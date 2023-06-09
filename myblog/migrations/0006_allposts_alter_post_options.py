# Generated by Django 4.0.1 on 2023-03-07 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_remove_post_image_post_news_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('intro', models.TextField()),
                ('img', models.FileField(default=None, max_length=250, null=True, upload_to='News')),
                ('data_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
    ]
