# Generated by Django 4.0.1 on 2023-03-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='writer_name',
            field=models.CharField(max_length=100),
        ),
    ]
