from django.apps import AppConfig

class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        from . import signals  # выполнение модуля -> регистрация сигналов
        from django.contrib import admin
        from .models import Category
        admin.site.register(Category)

