from django.views.generic import ListView, DetailView
from .models import Article, Gallery
from site_settings.models import SiteSetting
from django.shortcuts import get_object_or_404, render
from account.mixins import AuthorAccessMixin
# articles
def home_site(request):
    context = {
        'articles': Article.objects.published()[:3],
        'setting': SiteSetting.objects.first()
    }
    return render(request, 'blog/home_site.html', context)


class ArticleList(ListView):
    queryset = Article.objects.published()
    paginate_by = 5


class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article.objects.published(), slug=slug)
        return article


class ArticlePreview(AuthorAccessMixin, DetailView):
    def get_object(self):
        pk = self.kwargs.get('pk')
        article = get_object_or_404(Article, pk=pk)
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