from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import RestaurantListView, RestaurantSpecificView, FoodSpecificView

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='api-restaurants'),
    path('restaurants/<uuid:uuid>/', RestaurantSpecificView.as_view(), name='api-specific-restaurants'),
    path('foods/<uuid:uuid>/', FoodSpecificView.as_view(), name='api-specific-foods'),
]