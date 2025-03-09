from tabnanny import verbose

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import format_html
from django.utils.text import slugify
from  django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class ArticleManager(models.Manager):
    def counter(self):
        return len(self.all())

    def published(self):
        return self.filter(published=True)

class Article(models.Model):
    CHOICES = (
        ('A','پایتون'),
        ('B', 'جنگو')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', verbose_name='نویسنده ی مقالات')
    title = models.CharField(max_length=70, choices = CHOICES, default='A', verbose_name='عنوان')
    category = models.ManyToManyField(Category, related_name='articles', verbose_name='دسته بندی')
    body = models.TextField(verbose_name='متن')
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی',)
    pub_date = models.DateField(default=timezone.now, verbose_name='تاریخ انتشار')
    objects = ArticleManager()
    slug = models.SlugField(max_length=70, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.id])


    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="100" height="100" />')
        return format_html(f'<p style="color:red">تصویر ندارد</p>')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'مقاله'
        verbose_name_plural ='مقالات'

    # def save(
    #     self,
    #     force_insert = ...,
    #     force_update = ...,
    #     using = ...,
    #     update_fields = ...,
    # ):
    #     self.slug = slugify(self.title)
    #     super(Article, self).save()

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.body[:30]} - {self.user}"

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'



class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    type = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural ='پیام ها'