# Generated by Django 3.1.7 on 2021-07-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210719_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=300, unique=True, verbose_name='آدرس مقاله'),
        ),
    ]
