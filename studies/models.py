from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class StudySession(models.Model):
    class Status(models.TextChoices):
        COMPLETED = 'completed', 'Tamamlandı'
        PARTIAL = 'partial', 'Kısmen Tamamlandı'
        DISTRACTED = 'distracted', 'Dikkat Dağıldı'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='study_sessions'
    )
    date = models.DateField()
    topic = models.CharField(max_length=255, blank=True, null=True)
    planned_duration = models.PositiveIntegerField(help_text="Dakika cinsinden")
    started_at = models.DateTimeField(auto_now_add=True)

    # Oturum bittiğinde doldurulacak alanlar
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        blank=True,
        null=True
    )
    difficulty = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        blank=True,
        null=True
    )
    actual_duration = models.PositiveIntegerField(
        help_text="Dakika cinsinden",
        blank=True,
        null=True
    )

    # Başka bir app tarafından hesaplanacak
    score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.topic or 'Konu yok'}"
