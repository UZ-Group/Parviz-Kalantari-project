from django.urls import path
from .views import (
    profile,
    AdminHome,
    ArticleCreate,
    ArticleUpdate,
    ArticleDelete
)

app_name = "account"
urlpatterns = [
    path('', AdminHome.as_view(), name='home'),
    path('profile/', profile, name='profile'),
    path('article/create', ArticleCreate.as_view(), name='article-create'),
    path('article/update/<int:pk>', ArticleUpdate.as_view(), name='article-update'),
    path('article/delete/<int:pk>', ArticleDelete.as_view(), name='article-delete'),
]