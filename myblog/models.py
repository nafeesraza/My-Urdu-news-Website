from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    news_img = models.FileField(upload_to = 'News',max_length=250, null= True, default=None)
    intro = models.TextField()
    body = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)


class Articles(models.Model):
    title = models.CharField(max_length=225)
    visual = models.FileField(upload_to = 'News',max_length=250, null= True, default=None)
    contnt = models.TextField(default=None) 
    writer_name = models.CharField(max_length=100) 
    phone = models.CharField(null=False, unique=True, max_length=10)
    writer_img = models.FileField(upload_to = 'Article',max_length=250, null= True, default=None)
    data_added = models.DateTimeField(auto_now_add=True)

class Meta:
        ordering = ['-data_added']
