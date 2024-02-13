from django.db import migrations, models


def add_category_foreign_key(apps, schema_editor):
    # Получаем доступ к моделям
    Post = apps.get_model('news', 'Post')
    Category = apps.get_model('news', 'Category')

    # Добавляем внешний ключ
    Post.objects.filter(category_id__isnull=True).update(category_id=1)


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),  # Укажите имя предыдущей миграции
    ]

    operations = [
        migrations.RunPython(add_category_foreign_key),  # Выполнить функцию добавления внешнего ключа
    ]
