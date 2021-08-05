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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = Article.objects.published().order_by("-hits")[:2]
        return context

class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article.objects.published(), slug=slug)

        ip_address = self.request.user.ip_address
        if ip_address not in article.hits.all():
            article.hits.add(ip_address)

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