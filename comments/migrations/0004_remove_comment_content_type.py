# Generated by Django 4.2.4 on 2023-08-20 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_remove_comment_object_id_comment_object_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='content_type',
        ),
    ]
