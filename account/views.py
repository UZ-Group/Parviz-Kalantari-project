from django.db import models
from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from blog.models import Article
from .mixins import FieldsMixin, FormValidMixin, AuthorAccessMixin , SuperUserAccessMixin

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


class ArticleUpdate(AuthorAccessMixin, FieldsMixin, FormValidMixin, UpdateView):
    model = Article
    template_name = 'myAdminPanel/article-create-update.html'


class ArticleDelete(SuperUserAccessMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('account:home')
    template_name = template_name = 'myAdminPanel/article_confirm_delete.html'