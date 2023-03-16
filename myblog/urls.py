from django.urls import path
from .views import * 
urlpatterns = [
    path('home/', home),
    path('article/',articles),
    path('ibadat/', ibadat),
    path('history/', history),
    path('quran/', quran),
    path('women/', women),
    path('articles/', allposts),
    path('<int:id>', detail_page, name="detail"),
]