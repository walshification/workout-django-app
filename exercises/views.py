from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

# from exercises.forms import NewWorkoutForm
from exercises.models import Routine, Workout


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


class CreateWorkout(FormView):
    """Start a new workout for a given routine."""

    model = Workout
    # form_class = NewWorkoutForm
    success_url = reverse_lazy("exercises:active_workout")

    def form_valid(self, form):
        """Verify we have a routine to make the workout out of."""
        if form.is_valid():
            return super().form_valid(form)
