from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from  django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=70, choices = CHOICES, default='A')
    category = models.ManyToManyField(Category, related_name='articles')
    body = models.TextField()
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pub_date = models.DateField(default=timezone.now)
    objects = ArticleManager()
    slug = models.SlugField(max_length=70, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.id])

    class Meta:
        ordering = ('-created',)

    def save(
        self,
        force_insert = ...,
        force_update = ...,
        using = ...,
        update_fields = ...,
    ):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"
