from django.contrib import admin
from django.contrib.admin.sites import site
from myblog.models import Post
from myblog.models import Articles

class NewsAdmin(admin.ModelAdmin):
    list_display=("title","slug","data_added","news_img")

class ArticleAdmin(admin.ModelAdmin):
    list_display=("title","visual","contnt","writer_name","phone","writer_img","data_added")
# Register your models here.

from .models import Post
from .models import Articles
admin.site.register(Post, NewsAdmin)
admin.site.register(Articles, ArticleAdmin)
