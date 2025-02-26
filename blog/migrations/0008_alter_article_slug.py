# Generated by Django 5.1.6 on 2025-02-26 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, default=1, max_length=70, unique=True),
            preserve_default=False,
        ),
    ]
