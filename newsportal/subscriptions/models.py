from django.conf import settings
from django.db import models
from news.models import Category

class Subscriptions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} subscribed to {self.category}"

