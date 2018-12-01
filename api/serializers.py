from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer


from .models import Restaurant, Food, FoodOption


class UserSerializer(UserDetailsSerializer):

    uuid         = serializers.UUIDField(source="userprofile.uuid")
    phone_number = serializers.CharField(source="userprofile.phone_number")

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('phone_number', 'uuid',)

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile', {})
        phone_number = profile_data.get('phone_number')

        instance = super(UserSerializer, self).update(instance, validated_data)

        # get and update user profile
        profile = instance.userprofile
        if profile_data and phone_number:
            profile.phone_number = phone_number
            profile.save()
        return instance

class NearbyRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = (
            'distance',
            'uuid',
            'uuid_url',
            'name',
            'created_date',
            'created_datetime',
            'homepage_urllink',
            'rating',
            'description',
            'features',
            'cuisine',
            'email',
            'phone',
            'address',
            'post_code',
            'image_1',
            'image_2',
            'image_3',
            'video',
            'video_urllink',
            'open_day',
            'open_from_hour',
            'open_to_hour',
            'place_urllink',
            'longitude',
            'latitude',
            )

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class FoodOptionSpecificSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodOption
        fields = '__all__'


class FoodSpecificSerializer(serializers.ModelSerializer):
    food_foodoptions = FoodOptionSpecificSerializer(many=True, read_only=True)

    class Meta:
        model = Food
        fields = '__all__'


class RestaurantSpecificSerializer(serializers.ModelSerializer):
    restaurant_foods = FoodSpecificSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = '__all__'


