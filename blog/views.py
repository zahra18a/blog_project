from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from blog.forms import ContactUsForm, MessageForm
from blog.models import Article, Category, Comment, Message


def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    # article = get_object_or_404(Article,slug=slug)
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)

    return render(request, 'blog/article-details.html', context={'article': article})


def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/article_list.html', context={'articles': object_list})


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    # articles = category.article_set.all()
    articles = category.articles.all()  # با کمک related_name اوردیم بجای خط بالا
    return render(request, 'blog/article_list.html', context={'articles': articles})


def search(request):
    q = request.GET.get('q')
    title_map = {
        'پایتون': 'A',
        'جنگو': 'B'
    }

    q_translated = title_map.get(q, q)
    articles = Article.objects.filter(title__icontains=q_translated)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/article_list.html', context={'articles': object_list})


def contact_us(request):
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            # title = form.cleaned_data['title']
            # text = form.cleaned_data['text']
            # email = form.cleaned_data['email']
            # Message.objects.create(title=title, text=text, email=email)
            # form.save()-----> در این حالت داده ها رو در پایگاه داده مستقیم ذخیره میکند
            instance = form.save(commit=False)
            # -  در حالت داده ها را در پایگاه داده ذخیره نمیکند بلکه یک نمونه میسازد------
            instance.type = "کاربر"
            instance.save()
    else:
        form = MessageForm()
    return render(request, 'blog/contact_us.html', {'form': form})
