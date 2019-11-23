from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('home/', views.HomeView.as_view(), name = 'home'),
    path('create/', views.create, name = 'create'),
    path('click/<int:ad_id>/', views.RedirectToAdView.as_view(), name = 'redirectToAd'),
    path('stats/', views.StatsView.as_view(), name = 'stats'),

    path('api/ad_list', views.AdView.as_view({'get' : 'list'}), name = 'adList'),
    path('api/ad/<int:pk>/', views.AdView.as_view({'get' : 'retrieve'}), name = 'ad'),
    path('api/advertiser_list/', views.AdvertiserView.as_view({'get' : 'list'}), name = 'advertiserList'),
    path('api/advertiser/<int:pk>/', views.AdvertiserView.as_view({'get' : 'retrieve'}), name = 'advertiser'),
]
