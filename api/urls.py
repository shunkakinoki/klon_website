from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import RestaurantListView, RestaurantSpecificView, FoodSpecificView, FoodOptionSpecificView

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<uuid:uuid>/', RestaurantSpecificView.as_view(), name='restaurant-detail'),
    path('foods/<uuid:uuid>/', FoodSpecificView.as_view(), name='api-specific-foods'),
    path('foodoptions/<uuid:uuid>/', FoodOptionSpecificView.as_view(), name='api-specific-foods'),
]