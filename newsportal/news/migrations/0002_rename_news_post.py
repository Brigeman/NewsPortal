# Generated by Django 4.2.6 on 2023-11-09 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='Post',
        ),
    ]
