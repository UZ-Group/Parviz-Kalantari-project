from django.views.generic import ListView, DetailView
from .models import Article, Gallery
from django.shortcuts import get_object_or_404

# articles
class HomeSite(ListView):
    queryset = Article.objects.published()[:3]
    template_name = 'blog/home_site.html'


class ArticleList(ListView):
    queryset = Article.objects.published()
    paginate_by = 5


class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article.objects.published(), slug=slug)
        return article


# gallery
class GalleryList(ListView):
    queryset = Gallery.objects.all()
    paginate_by = 4


class GalleryDetail(DetailView):
    def get_object(self):
        paint_id = self.kwargs.get('id')
        paint = get_object_or_404(Gallery.objects.all(), id=paint_id)
        return paint