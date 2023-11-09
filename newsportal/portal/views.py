from django.shortcuts import render
from .models import Post

def news_list(request):
    news = Post.objects.all().order_by('-created_at')  # Сортировка от более свежей к старой
    return render(request, 'news_list.html', {'news': news})

def news_detail(request, article_id):
    article = Post.objects.get(pk=article_id)
    return render(request, 'news_detail.html', {'article': article})

