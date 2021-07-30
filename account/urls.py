from django.urls import path
from .views import (
    AdminHome,
    ArticleCreate,
    ArticleUpdate,
    ArticleDelete,
    Profile,
    UserPanel
)

app_name = "account"
urlpatterns = [
    path('', AdminHome.as_view(), name='home'),
    path('article/create', ArticleCreate.as_view(), name='article-create'),
    path('article/update/<int:pk>', ArticleUpdate.as_view(), name='article-update'),
    path('article/delete/<int:pk>', ArticleDelete.as_view(), name='article-delete'),
    path('profile/', Profile.as_view(), name='profile'),
    path('user-panel/', UserPanel.as_view(), name='user-panel'),
]