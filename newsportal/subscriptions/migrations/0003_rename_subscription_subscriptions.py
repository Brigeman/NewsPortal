# Generated by Django 4.2.6 on 2023-11-29 20:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20231128_2149'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscriptions', '0002_subscription_delete_subscriber'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscription',
            new_name='Subscriptions',
        ),
    ]