from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView

from exercises.forms import CreateWorkoutForm, UpdateWorkoutForm
from exercises.models import Exercise, Routine, Set, Workout


class Register(FormView):
    """Sign up!"""

    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("exercises:index")
    template_name = "register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


def redirect_to_login(request):
    """Redirect to the index or login page."""
    return redirect(reverse("exercises:index"))


@login_required
def index(request):
    """Just display a page."""
    return render(request, "exercises/index.html")


class RoutineList(LoginRequiredMixin, ListView):
    """Displays a user's routines in a table."""

    model = Routine

    def get_queryset(self) -> QuerySet[Routine]:
        """Defines the user's routines queryset."""
        return Routine.objects.filter(owner=self.request.user)


class CreateWorkout(LoginRequiredMixin, FormView):
    """Start a new workout for a given routine."""

    form_class = CreateWorkoutForm
    template_name = "exercises/workout_form.html"
    success_url = reverse_lazy("exercises:active_workout")

    def get_form(self, *args, **kwargs):
        routines = self.request.user.routines.all()
        form = super().get_form(*args, **kwargs)
        form.fields["routine"].choices = [("", "--------")] + list(
            (routine.name, routine.name) for routine in routines
        )
        return form

    def form_valid(self, form):
        """Verify we have a routine to make the workout out of."""
        if form.is_valid():
            Workout.objects.create(
                routine=Routine.objects.create()
            )
            form.instance.owner = self.request.user
            redirect(reverse("exercises:active_workout"))
        return render(
            self.request,
            reverse("exercises:create_workout"),
            {"form": form},
        )


class UpdateWorkout(LoginRequiredMixin, FormView):
    """Update the workout with the sets done."""

    form_class = UpdateWorkoutForm
    template_name = "exercises/active_workout.html"
    success_url = reverse_lazy("exercises:history")

    def get_context_data(self, **kwargs):
        """Prep data for the form."""
        data = super().get_context_data(**kwargs)
        data["exercises"] = []
        workout = Workout.objects.filter(
            owner=self.request.user, is_completed=False
        ).first()
        for exercise in workout.routine.exercises.all():
            data["exercises"].append(exercise)
        return data

    def form_valid(self, form):
        """Update!"""
        if form.is_valid():
            workout = Workout.objects.filter(
                owner=self.request.user, is_completed=False
            ).first()
            workout.completed_at = timezone.now()
            workout.is_completed = True
            workout.save()
            return super().form_valid(form)

        return render(
            self.request,
            reverse("exercises:active_workout"),
            {"form": form},
        )

    def form_invalid(self, form):
        return super().form_invalid(form)


class CreateSet(LoginRequiredMixin, CreateView):
    """Start a new set for a given exercise."""

    model = Set
    fields = ["weight", "reps"]
    success_url = reverse_lazy("exercises:active_workout")

    def form_valid(self, form):
        """Verify we have a routine to make the workout out of."""
        if form.is_valid():
            Exercise.objects.get(pk=int(self.kwargs["exercise_id"])).sets.add(
                Set.objects.create(
                    weight=form.cleaned_data["weight"],
                    reps=form.cleaned_data["reps"],
                )
            )
            return redirect(reverse("exercises:active_workout"))
        return render(
            self.request,
            reverse("exercises:create_set"),
            {"form": form},
        )
