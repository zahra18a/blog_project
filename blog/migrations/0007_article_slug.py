# Generated by Django 5.1.6 on 2025-02-26 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_category_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=70, null=True, unique=True),
        ),
    ]
