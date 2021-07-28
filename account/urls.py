from django.urls import path
from .views import (
    profile,
    AdminHome,
    ArticleCreate,
)

app_name = "account"
urlpatterns = [
    path('', AdminHome.as_view(), name='home'),
    path('profile/', profile, name='profile'),
    path('article/create', ArticleCreate.as_view(), name='article-create'),
]