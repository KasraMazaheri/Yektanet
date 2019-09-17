from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.Home, name = 'Home'),
    path('create/', views.Create, name = 'Create'),
    path('click/<int:ad_id>/', views.RedirectToAd, name = 'RedirectToAd'),
]
