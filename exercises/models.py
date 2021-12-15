from django.contrib.auth.models import User
from django.db import models


class Routine(models.Model):
    """A collection of exercises."""

    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="routines")


class Workout(models.Model):
    """An instance of working out to a routine."""

    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts")
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)


class Set(models.Model):
    """A runthrough of an exercise."""

    weight = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)


class Exercise(models.Model):
    """A particular exercise in a routine."""

    name = models.CharField(max_length=200)
    routine = models.ForeignKey(
        Routine, on_delete=models.CASCADE, related_name="exercises"
    )
    sets = models.ManyToManyField(Set, related_name="sets")
