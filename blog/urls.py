from django.urls import path
from . import  views

app_name = 'blog'
urlpatterns = [
   # path('detail/<int:pk>', views.article_detail, name='article_detail'),
   path('detail/<slug:slug>', views.article_detail, name='article_detail'),
   path('list', views.article_list, name='article_list'),

]