from django.db import models
from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView
from blog.models import Article
from .mixins import FieldsMixin, FormValidMixin

# Create your views here.
class Login(LoginView):
    pass


def profile(request):
    return HttpResponse("this is profile {}".format(request.user.username))


class AdminHome(LoginRequiredMixin, ListView):
    template_name = 'myAdminPanel/home.html'
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)


class ArticleCreate(LoginRequiredMixin, FieldsMixin, FormValidMixin, CreateView):
    model = Article
    template_name = 'myAdminPanel/article-create-update.html'