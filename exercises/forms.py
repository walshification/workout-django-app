from django import forms

from exercises.models import Workout


class CreateWorkoutForm(forms.Form):
    """Form for creating a workout from a routine."""

    routine = forms.ChoiceField()


class UpdateWorkoutForm(forms.Form):
    """Form for updating the progress of a workout."""

    is_completed = forms.BooleanField()


class CreateSetForm(forms.Form):
    """Create a set for an exercise."""

    weight = forms.IntegerField()
    reps = forms.IntegerField()
    exercise_id = forms.IntegerField()
