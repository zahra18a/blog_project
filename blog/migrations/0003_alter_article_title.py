# Generated by Django 5.1.6 on 2025-02-19 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(choices=[('A', 'پایتون'), ('B', 'جنگو')], max_length=70),
        ),
    ]
