# Generated by Django 3.1.7 on 2021-07-19 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان مقاله')),
                ('slug', models.SlugField(max_length=300, verbose_name='آدرس مقاله')),
                ('image', models.ImageField(upload_to='images', verbose_name='تصویر مقاله')),
                ('description', models.TextField(verbose_name='متن مقاله')),
                ('short_des', models.TextField(max_length=500, verbose_name='خلاصه مقاله')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('d', 'پیش\u200cنویس'), ('p', 'منتشر شده'), ('i', 'درحال بررسی'), ('b', 'برگشت داده شده')], max_length=1, verbose_name='وضعیت')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
        ),
    ]
