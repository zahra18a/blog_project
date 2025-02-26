from django.shortcuts import render
from blog.models import Article
def home(request):
    articles = Article.objects.all()
    print(Article.objects.counter())
    recent_articles = Article.objects.all().order_by('-created')[:3]
    return render(request,"home/index.html",context={'articles':articles, 'recent_articles':recent_articles})
