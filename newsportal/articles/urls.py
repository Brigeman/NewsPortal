from django.urls import path
from .views import ArticlesCreateView, ArticlesDeleteView, ArticlesUpdateView, ArticlesListView


urlpatterns = [
    path('', ArticlesListView.as_view(), name='articles_list'),
    path('create/', ArticlesCreateView.as_view(), name='articles_create'),
    path('<int:pk>/edit/', ArticlesUpdateView.as_view(), name='articles_edit'),
    path('<int:pk>/delete/', ArticlesDeleteView.as_view(), name='articles_delete'),
]