from blog.models import  Article, Category

def recent_articles(request):
    recent = Article.objects.order_by('-created')[:5]
    return {'recent_articles': recent}

def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}