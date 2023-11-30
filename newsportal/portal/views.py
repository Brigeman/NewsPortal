from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def news_list(request):
    news = Post.objects.all().order_by('-created_at')  # Сортировка от более свежей к старой
    paginator = Paginator(news_list, 10) # По 10 новостей на странице
    page = request.GET.get('page')

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # Если пагинатор не целое возвращаем страницу 1
        news = paginator.page(1)
    except EmptyPage:
        # Если номер страницы > чем страниц всего
        news = paginator.page(paginator.num_pages)

    return render(request, 'news_list.html', {'news': news})

def news_detail(request, article_id):
    article = Post.objects.get(pk=article_id)
    return render(request, 'news_detail.html', {'article': article})


def search_news(request):
    query = request.GET.get('q')
    if query:
        news_results = Post.objects.filter(
            Q(title__icontains=query) | Q(category__icontains=query) | Q(created_at__icontains=query)
        ).distinct().order_by('-created_at')
    else:
        news_results = []

    return render(request, 'portal/search_results.html', {'news_results': news_results})

