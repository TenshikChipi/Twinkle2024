from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index),
    path('autumn',views.autumn),
    path('colottype',views.colottype), 
    path('log',views.log),
    path('razdeli',views.razdeli),
    path('spring',views.spring),
    path('summer',views.summer),
    path('winter',views.winter),
]    
