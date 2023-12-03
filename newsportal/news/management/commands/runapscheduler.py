import logging
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

from news.models import Post
from subscriptions.models import Subscriptions

logger = logging.getLogger(__name__)


def my_job():
    subscriptions = Subscriptions.objects.all()

    for subscription in subscriptions:
        category = subscription.category
        subscribed_users = User.objects.filter(subscriptions__category=category)

        new_articles = Post.objects.filter(category=category)

        for user in subscribed_users:
            user_email = user.email
            user_articles = new_articles.filter(created_at__gte=subscription.last_notification_date)

            if user_articles.exists():
                subject = f'New articles in {category.name}'
                message = '\n'.join([f'{article.title}: {article.content}\n'
                                     f'{settings.BASE_URL}{reverse("news_detail", args=[article.id])}'
                                     for article in user_articles])

                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])


                subscription.last_notification_date = Post.objects.latest('created_at').created_at
                subscription.save()


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(day_of_week="fri", hour="18", minute="00"),
            id="my_job",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added weekly job: 'my_job'.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")

