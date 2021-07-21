from django.contrib import admin
from .models import Article, Gallery
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image_tag', 'author', 'jpublish','status')
    list_filter = ('status', 'publish', 'author')
    search_fields = ('title', 'description')
    ordering = ('-status', '-publish')


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('__str__','image_tag')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Gallery, GalleryAdmin)