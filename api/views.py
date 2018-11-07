from rest_framework import generics
from .models import Restaurant, Food, FoodOption
from .serializers import RestaurantSerializer, FoodSerializer, FoodOptionSerializer

class RestaurantRUView(generics.RetrieveUpdateAPIView):
    lookup_field        = 'uuid'
    serializer_class    = RestaurantSerializer

    def get_queryset(self):
        return Restaurant.objects.all()

class FoodRUView(generics.RetrieveUpdateAPIView):
    lookup_field        = 'uuid'
    serializer_class    = FoodSerializer

    def get_queryset(self):
        return Food.objects.all()

class FoodOptionRUView(generics.RetrieveUpdateAPIView):
    lookup_field        = 'uuid'
    serializer_class    = FoodOptionSerializer

    def get_queryset(self):
        return FoodOption.objects.all()