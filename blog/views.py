from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category
from django.core.paginator import Paginator


def article_detail(request, slug):
    # article = Article.objects.get(id=pk)
    article = get_object_or_404(Article,slug=slug)
    return render(request, 'blog/article-details.html', context={'article': article})

def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(page_number)
    return render(request,'blog/article_list.html', context={'articles':object_list})

def category_detail(request, pk=None):
    category = get_object_or_404(Category,id=pk)
    # articles = category.article_set.all()
    articles=category.articles.all() #با کمک related_name اوردیم بجای خط بالا
    return render(request, 'blog/article_list.html', context={'articles': articles})