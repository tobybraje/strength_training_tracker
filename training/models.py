from django.db import models
from django_extensions.db.models import TimeStampedModel

from users.models import User


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, default="Add exercise description here")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_exercises", null=True, blank=True)


class WorkOut(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, default="Add workout description here")
    exercises = models.ManyToManyField(Exercise, related_name="member_workouts")
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="owned_workouts")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_workouts", null=True, blank=True)


class Set(TimeStampedModel):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    reps = models.IntegerField()
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="sets")
