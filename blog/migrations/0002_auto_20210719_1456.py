# Generated by Django 3.1.7 on 2021-07-19 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-publish'], 'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='published',
            new_name='publish',
        ),
    ]
