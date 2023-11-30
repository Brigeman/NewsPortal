from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title

