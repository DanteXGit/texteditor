# Generated by Django 3.0.7 on 2020-06-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20200608_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='PostSlug',
            field=models.SlugField(default='Slug', verbose_name='Слаг файла'),
        ),
    ]
