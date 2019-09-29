from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('home/', views.HomeView.as_view(), name = 'home'),
    path('create/', views.create, name = 'create'),
    path('click/<int:ad_id>/', views.RedirectToAdView.as_view(), name = 'redirectToAd'),
    path('stats/', views.StatsView.as_view(), name = 'stats'),
]
