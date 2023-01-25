from django.urls import path

from shorturlapp import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('shorter/', views.short, name="shorter"),
    path('output/', views.retrieve, name="virivu"),
]