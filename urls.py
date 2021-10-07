from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'), #generic path, look for function home in views.py, name it as blog-hom, to differentiate from toehr home
    path('about/', views.about, name='blog-about'),
] 