# Generated by Django 5.0.7 on 2024-07-20 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_comment_author_alter_comment_created_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="author",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]