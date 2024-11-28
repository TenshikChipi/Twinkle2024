from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index),
    path('',views.autumn),
    path('',views.colottype), 
    path('',views.log),
    path('',views.razdeli),
    path('',views.spring),
    path('',views.summer),
    path('',views.winter),
]    