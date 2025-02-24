from django.shortcuts import render
from blog.models import Article
def home(request):
    articles = Article.objects.published()
    print(Article.objects.counter())
    return render(request,"home/index.html",context={'articles':articles})
