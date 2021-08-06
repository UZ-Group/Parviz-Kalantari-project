from django.urls import path
from .views import (
    home_site,
    ArticleList,
    ArticleDetail,
    GalleryList,
    GalleryDetail,
    ArticlePreview,
    VideoList,
    VideoDetail,
    like
)

app_name = 'blog'
urlpatterns = [
    path('', home_site, name='home_site'),
    path('articles/', ArticleList.as_view(), name='article_list'),
    path('articles/page/<int:page>', ArticleList.as_view(), name='article_list'),
    path('article/<slug:slug>', ArticleDetail.as_view(), name='article_detail'),
    path('article/<int:pk>/like', like, name='like'),
    path('preview/<int:pk>', ArticlePreview.as_view(), name='preview'),
    path('gallery/', GalleryList.as_view(), name='gallery'),
    path('gallery/page/<int:page>', GalleryList.as_view(), name='gallery'),
    path('gallery/<int:id>', GalleryDetail.as_view(), name='gallery_detail'),
    path('video/', VideoList.as_view(), name='video'),
    path('video/page/<int:page>', VideoList.as_view(), name='video'),
    path('video/<int:pk>', VideoDetail.as_view(), name='video_detail'),
]
