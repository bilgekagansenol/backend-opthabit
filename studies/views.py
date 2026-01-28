from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import StudySession
from .serializers import (
    StudySessionSerializer,
    StudySessionCreateSerializer,
    StudySessionCompleteSerializer
)


class StudySessionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = StudySessionSerializer

    def get_queryset(self):
        return StudySession.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return StudySessionCreateSerializer
        if self.action == 'complete':
            return StudySessionCompleteSerializer
        return StudySessionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        """Oturumu tamamla ve değerlendir"""
        session = self.get_object()

        if session.status:
            return Response(
                {"detail": "Bu oturum zaten tamamlanmış."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Geçen süreyi hesapla (dakika cinsinden)
        elapsed = timezone.now() - session.started_at
        elapsed_minutes = int(elapsed.total_seconds() // 60)

        # Planlanan süreden fazla geçtiyse, planned_duration kullan
        actual_duration = min(elapsed_minutes, session.planned_duration)

        serializer = self.get_serializer(session, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(actual_duration=actual_duration)

        return Response(StudySessionSerializer(session).data)
