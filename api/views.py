from rest_framework import generics
from .models import Restaurant, Food, FoodOption
from .serializers import RestaurantSerializer, RestaurantSpecificSerializer, FoodSpecificSerializer
from django.db.models import Q

class RestaurantListView(generics.ListAPIView):
    serializer_class    = RestaurantSerializer

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