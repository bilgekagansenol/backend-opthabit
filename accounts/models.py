from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)

    # Mobil uygulama için ek alanlar (ileride genişletilebilir)
    # google_id = models.CharField(max_length=255, blank=True, null=True)
    # is_email_verified = models.BooleanField(default=False)
    # profile_picture = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
