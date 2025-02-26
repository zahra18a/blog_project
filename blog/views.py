from django.shortcuts import render, get_object_or_404
from blog.models import Article


def article_detail(request, pk):
    # article = Article.objects.get(id=pk)
    article = get_object_or_404(Article,id=pk)
    return render(request, 'blog/article-details.html', context={'article': article})
