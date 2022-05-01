from django.contrib import admin
from django.urls import path
from Dept import views

urlpatterns = [
    path('',views.home),
    path('CS',views.cs),
    path('IS',views.IS),
    path('reg',views.reg),
    path('EC',views.ec)
]