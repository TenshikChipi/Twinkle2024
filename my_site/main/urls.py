from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.aboutus),
    path('',views.colortp),
    path('',views.colottypetest), 
    path('',views.log),
    path('',views.menu),
    path('',views.otcek),
    path('',views.sign),
    path('',views.spring),
    path('',views.summer),
    path('',views.wardrob),
    path('',views.winter),
] 
