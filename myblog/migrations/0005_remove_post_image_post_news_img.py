# Generated by Django 4.0.1 on 2023-02-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='news_img',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='News'),
        ),
    ]