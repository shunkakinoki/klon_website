from django.contrib import admin
from django.urls import path
from .views import RestaurantRUView, FoodRUView, FoodOptionRUView

urlpatterns = [
    path('restaurant/<uuid:uuid>/', RestaurantRUView.as_view(), name='api-restaurant'),
    path('food/<uuid:uuid>/', FoodRUView.as_view(), name='api-food'),
    path('foodoption/<uuid:uuid>/', FoodOptionRUView.as_view(), name='api-food'),
]