from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.about, name='aboutus'),
    path('wardrob/', views.wardrobe, name='wardrob'),
    path('log/', auth_views.LoginView.as_view(), name='log'),
    path('sign/', auth_views.LogoutView.as_view(), name='sign'),
    path('menu/', views.about, name='menu'),
    path('otcek/', views.about, name='otcek'),
    path('autumn/', views.autumn, name='autumn'),
    path('winter/', views.winter, name='awinter'),
    path('spring/', views.spring, name='spring'),
    path('summer/', views.summer, name='summer'),
]
