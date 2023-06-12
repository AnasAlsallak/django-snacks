from django.contrib import admin
from django.urls import path
from snacks.views import HomePageView, AboutPageView #or .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(),name='about'),
]
