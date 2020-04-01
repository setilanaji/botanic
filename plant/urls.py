from django.urls import include, path
from django.shortcuts import render
from rest_framework import routers
from . import views


urlpatterns = [
    path('', views.ListPlant.as_view()),
    path('<int:pk>/', views.DetailPlant.as_view()),
    path('rest-auth/', include(('rest_auth.urls', 'rest_auth'))),
]
