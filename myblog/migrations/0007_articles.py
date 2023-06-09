# Generated by Django 4.0.1 on 2023-03-09 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_allposts_alter_post_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('writer_name', models.TextField()),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('img', models.FileField(default=None, max_length=250, null=True, upload_to='Article')),
                ('data_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
