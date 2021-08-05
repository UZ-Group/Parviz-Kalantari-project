from django.db import models
from django.urls import reverse
from account.models import User
from django.utils import timezone
from django.utils.html import format_html
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from extensions.utils import jalali_converter
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment

# my managers
class ArticleManager(models.Manager):
    def published(self):
        return Article.objects.filter(status='p')


# Create your models here.
class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="آدرس آی‌پی")


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),           #draft
        ('p', 'منتشر شده'),        #publish
        ('i', 'درحال بررسی'),     #investigation
        ('b', 'برگشت داده شده'), #back
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles', verbose_name='نویسنده')
    title = models.CharField(max_length=300, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=300, unique=True, allow_unicode=True, verbose_name='آدرس مقاله')
    image = models.ImageField(upload_to='images', verbose_name='تصویر مقاله')
    description = RichTextUploadingField(verbose_name='متن مقاله')
    short_des = models.TextField(max_length=500 ,verbose_name='خلاصه مقاله')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')
    comments = GenericRelation(Comment)
    hits = models.ManyToManyField(IPAddress, blank=True, related_name='hits', verbose_name='بازدیدها')
    likes = models.ManyToManyField(User, blank=True, related_name='likes', verbose_name='پسندیدن')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ["-publish"]


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('account:home')

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = 'زمان انتشار'

    def image_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 10px;' src='{}'>".format(self.image.url))
    image_tag.short_description = "عکس"

    objects = ArticleManager()
     
def article_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(article_pre_save_receiver, sender=Article)


class Gallery(models.Model):
    image = models.ImageField(upload_to='images/gallery', verbose_name='نقاشی')
    description = models.TextField(verbose_name='درباره نقاشی')

    class Meta:
        verbose_name = 'نقاشی'
        verbose_name_plural = 'گالری نقاشی ها'
    
    def image_tag(self):
        return format_html("<img width=250 height=150 style='border-radius: 10px;' src='{}'>".format(self.image.url))
    image_tag.short_description = "عکس"
