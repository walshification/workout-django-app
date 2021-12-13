from django.contrib.auth.models import User
from django.db import models


class Routine(models.Model):
    """A collection of exercises."""

    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="routines")


class Exercise(models.Model):
    """A particular exercise in a routine."""

    name = models.CharField(max_length=200)
    weight = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)
    routine = models.ManyToManyField(Routine, related_name="exercises")
