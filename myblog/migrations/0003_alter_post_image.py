# Generated by Django 4.0.1 on 2023-02-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_post_image_alter_post_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
