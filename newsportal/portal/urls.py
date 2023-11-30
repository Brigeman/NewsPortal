from django.urls import path
from .views import search_news, news_detail

urlpatterns = [
    path('portal/search/', search_news, name='search_news'),
    path('<int:pk>/detail/', news_detail, name='news_details'),
]
