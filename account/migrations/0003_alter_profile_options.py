# Generated by Django 5.1.6 on 2025-03-09 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'حساب کاربری', 'verbose_name_plural': 'حساب کاربران'},
        ),
    ]
