# Generated by Django 3.2.5 on 2021-08-07 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='receive_email',
            field=models.BooleanField(default=False, verbose_name='دریافت ایمیل برای هر مقاله جدید'),
        ),
    ]
