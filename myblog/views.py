from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .models import Articles
# Create your views here.
def home(request):
    res=render(request, 'home_page.html')
    return HttpResponse(res)
def allposts(request):
    posts = Articles.objects.all()
    return render(request, 'all_articles.html', {'posts': posts})

def articles(request):
    posts = Post.objects.all()
    return render(request, 'article_page.html', {'posts': posts})

def detail_page(request,id):
    obj = get_object_or_404(Articles, pk=id)
    return render(request, 'detail.html', {'obj':obj})

def ibadat(request):
    res=render(request, 'ibadat.html')
    return HttpResponse(res)

def history(request):
    res=render(request, 'islamic_history.html')
    return HttpResponse(res)

def quran(request):
    posts = Post.objects.all()
    return render(request, 'quran_k_ahkam.html', {'posts': posts})

def women(request):
    res=render(request, 'bint_e_hawwa.html')
    return HttpResponse(res)