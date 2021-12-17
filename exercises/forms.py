from django import forms


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


class CreateRoutineForm(forms.Form):
    """Create a routine."""

    name = forms.CharField(max_length=200)
    exercises = forms.CharField(
        max_length=500, help_text="Comma separated list of exercises"
    )
