from rest_framework import serializers

from .models import Restaurant, Food, FoodOption

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class FoodSpecificSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class RestaurantSpecificSerializer(serializers.ModelSerializer):
    restaurant_foods = FoodSpecificSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = '__all__'


class FoodOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodOption
        fields = '__all__'
