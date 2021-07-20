from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'jpublish','status')
    list_filter = ('status', 'publish', 'author')
    search_fields = ('title', 'description')
    ordering = ('-status', '-publish')

admin.site.register(Article, ArticleAdmin)