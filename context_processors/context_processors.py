from blog.models import  Article

def recent_articles(request):
    recent = Article.objects.order_by('-created')[:5]
    return {'recent_articles': recent}