from django.http.response import Http404
from django.views.generic import ListView, DetailView
from .models import Article, Gallery, Video
import random
from site_settings.models import SiteSetting
from django.shortcuts import get_object_or_404, redirect, render
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = random.sample(list(Article.objects.published()), 3)
        return context

def like(request, pk):
    user = request.user
    article = get_object_or_404(Article, pk=pk)
    if user.is_authenticated:
        if user in article.likes.all():
            article.likes.remove(user)
        else:
            article.likes.add(user)
        return redirect('blog:article_detail', article.slug)
    else:
        raise Http404('شما دسترسی به این صفحه ندارید!')


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

# videos
class VideoList(ListView):
    queryset = Video.objects.all()
    paginate_by = 2


class VideoDetail(DetailView):
    def get_object(self):
        pk = self.kwargs.get('pk')
        video = get_object_or_404(Video, pk=pk)
        return video