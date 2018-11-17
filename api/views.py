from rest_framework import generics
from .models import Restaurant, Food, FoodOption
from .serializers import (
    RestaurantSerializer,
    RestaurantSpecificSerializer,
    FoodSpecificSerializer,
    FoodOptionSpecificSerializer
)
from django.db.models import Q
from rest_framework import filters


class RestaurantListView(generics.ListAPIView):
    serializer_class = RestaurantSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'name',
        'cuisine',
        'features',
        'description',
        'restaurant_foods__name',
        'restaurant_foods__cuisine',
        'restaurant_foods__features',
        'restaurant_foods__description',
        'restaurant_foods__food_foodoptions__name',
        'restaurant_foods__food_foodoptions__description'
    )

    def get_queryset(self):
        return Restaurant.objects.all()

class RestaurantSpecificView(generics.RetrieveAPIView):
    lookup_field        = 'uuid'
    serializer_class    = RestaurantSpecificSerializer

    def get_queryset(self):
        qs = Restaurant.objects.all()
        query = self.request.GET.get("uuid")
        if query is not None:
            qs = qs.filter(
                Q(uuid__iexact=query)
            )
        return qs

class FoodSpecificView(generics.RetrieveAPIView):
    lookup_field        = 'uuid'
    serializer_class    = FoodSpecificSerializer

    def get_queryset(self):
        qs = Food.objects.all()
        query = self.request.GET.get("uuid")
        if query is not None:
            qs = qs.filter(
                Q(uuid__iexact=query)
            )
        return qs

class FoodOptionSpecificView(generics.RetrieveAPIView):
    lookup_field        = 'uuid'
    serializer_class    = FoodOptionSpecificSerializer

    def get_queryset(self):
        qs = FoodOption.objects.all()
        query = self.request.GET.get("uuid")
        if query is not None:
            qs = qs.filter(
                Q(uuid__iexact=query)
            )
        return qs