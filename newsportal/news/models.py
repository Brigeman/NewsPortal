from django.db import models

class Post(models.Model):
    # Ваши поля модели
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class News(Post):
    category = models.CharField(max_length=50)
    # Дополнительные поля для новости