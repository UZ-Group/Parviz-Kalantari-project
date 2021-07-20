from django.urls import path
from .views import HomeSite, ArticleList, ArticleDetail

app_name = 'blog'
urlpatterns = [
    path('', HomeSite.as_view(), name='home_site'),
    path('articles/', ArticleList.as_view(), name='article_list'),
    path('article/<slug:slug>', ArticleDetail.as_view(), name='article_detail'),
]
