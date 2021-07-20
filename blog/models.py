from django.db import models
from account.models import User
from django.utils import timezone
from extensions.utils import jalali_converter

# my managers
class ArticleManager(models.Manager):
    def published(self):
        return Article.objects.filter(status='p')


# Create your models here.
class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),           #draft
        ('p', 'منتشر شده'),        #publish
        ('i', 'درحال بررسی'),     #investigation
        ('b', 'برگشت داده شده'), #back
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles', verbose_name='نویسنده')
    title = models.CharField(max_length=300, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=300, unique=True, verbose_name='آدرس مقاله')
    image = models.ImageField(upload_to='images', verbose_name='تصویر مقاله')
    description = models.TextField(verbose_name='متن مقاله')
    short_des = models.TextField(max_length=500 ,verbose_name='خلاصه مقاله')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ["-publish"]


    def __str__(self):
        return self.title
    
    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = 'زمان انتشار'

    objects = ArticleManager()
    