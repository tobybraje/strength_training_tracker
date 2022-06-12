from django.db import models
from django_extensions.db.models import TimeStampedModel


class User(TimeStampedModel):
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=30)
