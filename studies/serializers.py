from rest_framework import serializers
from .models import StudySession


class StudySessionCreateSerializer(serializers.ModelSerializer):
    """Oturum başlatırken kullanılır"""

    class Meta:
        model = StudySession
        fields = ('id', 'date', 'topic', 'planned_duration', 'created_at')
        read_only_fields = ('id', 'created_at')


class StudySessionCompleteSerializer(serializers.ModelSerializer):
    """Oturum bittiğinde değerlendirme için kullanılır"""

    class Meta:
        model = StudySession
        fields = ('status', 'difficulty')

    def validate(self, attrs):
        if not attrs.get('status'):
            raise serializers.ValidationError({"status": "Oturum durumu zorunludur."})
        return attrs


class StudySessionSerializer(serializers.ModelSerializer):
    """Tam oturum detayı"""

    class Meta:
        model = StudySession
        fields = (
            'id', 'date', 'topic', 'planned_duration', 'started_at',
            'status', 'difficulty', 'actual_duration', 'score',
            'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'started_at', 'actual_duration', 'score', 'created_at', 'updated_at')
