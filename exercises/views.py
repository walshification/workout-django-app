from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


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
    return render(request, "exercises/index.html")
