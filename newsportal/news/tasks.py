from celery import shared_task
from django.core.mail import send_mail
from .models import Post
from subscriptions.models import Subscriptions
from django.conf import settings
from datetime import timedelta
from django.utils import timezone

@shared_task
def notify_subscribers_about_news(post_id):
    post = Post.objects.get(id=post_id)
    subscriptions = Subscriptions.objects.filter(category=post.category)

    for subscription in subscriptions:
        # Отправка уведомления на почту каждому подписчику категории новости
        send_mail(
            'Новая новость!',
            f'Появился новый пост: {post.title}',
            settings.DEFAULT_FROM_EMAIL,
            [subscription.user.email],  # Отправить на адрес пользователя, подписанного на категорию
            fail_silently=False,
        )



@shared_task
def send_weekly_newsletter():
    week_ago = timezone.now() - timedelta(days=7)
    latest_news = Post.objects.filter(created_at__gte=week_ago)

    for news in latest_news:
        subscriptions = Subscriptions.objects.filter(category=news.category)

        for subscription in subscriptions:
            # Отправка еженедельной рассылки новостей подписчикам категории
            send_mail(
                'Еженедельная рассылка новостей!',
                f'Последние новости: {news.title}',
                settings.DEFAULT_FROM_EMAIL,
                [subscription.user.email],  # Отправить на адрес пользователя, подписанного на категорию
                fail_silently=False,
            )
