from django.views.generic import ListView, DetailView
from .models import Article
from django.shortcuts import get_object_or_404
# Create your views here.

class HomeSite(ListView):
    queryset = Article.objects.published()[:3]
    template_name = 'blog/home_site.html'


class ArticleList(ListView):
    queryset = Article.objects.published()[:5]
    template_name = 'blog/article_list.html'


class ArticleDetail(DetailView):
    template_name = 'blog/article_detail.html'
    def get_object(self):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article.objects.published(), slug=slug)
        return article
    