from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from exercises.models import Routine


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


@login_required
def index(request):
    """Just display a page."""
    return render(request, "exercises/index.html")


class RoutineList(ListView):
    """Displays a user's routines in a table."""

    model = Routine

    def get_queryset(self) -> QuerySet[Routine]:
        """Defines the user's routines queryset."""
        return Routine.objects.filter(owner=self.request.user)
