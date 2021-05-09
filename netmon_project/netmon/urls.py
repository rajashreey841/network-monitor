from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='netmon-default'),
    path('home/', views.home, name='netmon-home'),
    path('about/', views.about, name='netmon-about'),
]