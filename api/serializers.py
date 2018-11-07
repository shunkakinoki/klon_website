from rest_framework import serializers

from .models import Restaurant, Food, FoodOption

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'uuid',             
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
        ]       


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'uuid',            
            'restaurant',      
            'name',            
            'created_date',    
            'created_datetime',
            'rating',          
            'description',     
            'features',        
            'cuisine',         
            'price',           
            'number',          
            'boolean',         
            'image_1',
            'image_2',
            'image_3',
            'video',  
            'video_urllink',       
        ]       


class FoodOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodOption
        fields = [
            'uuid',            
            'food',            
            'name',            
            'created_date',    
            'created_datetime',
            'description',     
            'price',           
            'number',          
            'boolean',         
            'image_1',
            'image_2',
            'image_3',
            'video',           
            'video_urllink',         
        ] 
