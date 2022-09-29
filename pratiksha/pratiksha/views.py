from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView


def home(request):
    return render(request, "Home.html")


def login(request):
    return render(request, "login.html")


class Register(CreateView):
    form_class = UserCreationForm
    success_url = "/login"
    template_name = "registration/register.html"

