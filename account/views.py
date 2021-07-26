from django.shortcuts import render, HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic import ListView

# Create your views here.
class Login(LoginView):
    pass


def profile(request):
    return HttpResponse("this is profile {}".format(request.user.username))