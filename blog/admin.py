from django.contrib import admin
from .models import Article, Gallery, IPAddress, Video

# Register your models here.
def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = "منتشر شد"
    else:
        message_bit = "منتشر شدند"
    modeladmin.message_user(request , "{} مقاله {}".format(rows_updated, message_bit) )
make_published.short_description = 'انتشار مقالات انتخاب شده'

@admin.action(description='پیش‌نویس شدن مقالات انتخاب شده')
def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated == 1:
        message_bit = "پیش‌نویس شد"
    else:
        message_bit = "پیش‌نویس شدند"
    modeladmin.message_user(request , "{} مقاله {}".format(rows_updated, message_bit) )

@admin.action(description='مقالات انتخاب شده را در حال بررسی قرار بده')
def make_investigation(modeladmin, request, queryset):
    rows_updated = queryset.update(status='i')
    if rows_updated == 1:
        message_bit = "در حال بررسی قرار داده شد"
    else:
        message_bit = "در حال بررسی قرار داده شدند"
    modeladmin.message_user(request , "{} مقاله {}".format(rows_updated, message_bit) )

@admin.action(description='برگشت دادن مقالات انتخاب شده')
def make_back(modeladmin, request, queryset):
    rows_updated = queryset.update(status='b')
    if rows_updated == 1:
        message_bit = "برگشت داده شد"
    else:
        message_bit = "برگشت داده شدند شدند"
    modeladmin.message_user(request , "{} مقاله {}".format(rows_updated, message_bit) )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image_tag', 'author', 'jpublish','status')
    list_filter = ('status', 'publish', 'author')
    search_fields = ('title', 'description')
    ordering = ('-status', '-publish')
    actions = [make_published, make_draft, make_investigation, make_back]


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('__str__','image_tag')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('__str__','image_tag', 'jpublish')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(IPAddress)