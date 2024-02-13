from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post

from .tasks import notify_subscribers_about_news


@receiver(post_save, sender=Post)
def news_add(instance, created, **kwargs):
    if not created:
        return

    emails = User.objects.filter(
        subscriptions__category=instance.category
    ).values_list('email', flat=True)

    subject = f'Новая новость {instance.category}'

    text_content = (
        f'Ссылка на новость: http://127.0.0.1:8000{instance.get_absolute_url()}' # временная ссылка
    )
    html_content = (
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'# временная ссылка 
        f'Ссылка на новость</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


@receiver(post_save, sender=Post)
def send_notification_to_subscribers(sender, instance, created, **kwargs):
    if created:
        notify_subscribers_about_news.delay(instance.id)