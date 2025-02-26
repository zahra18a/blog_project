from django.shortcuts import render
from blog.models import Article
def home(request):
    articles = Article.objects.all()
    print(Article.objects.counter())
    return render(request,"home/index.html",context={'articles':articles})
