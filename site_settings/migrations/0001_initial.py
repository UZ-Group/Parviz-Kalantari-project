# Generated by Django 3.1.7 on 2021-07-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(verbose_name='بیوگرافی')),
                ('image', models.ImageField(upload_to='images/site', verbose_name='عکس هنرمند(بیو)')),
                ('contact_us', models.TextField(verbose_name='ارتباط با ما')),
            ],
        ),
    ]
