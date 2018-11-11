from django.contrib import admin

from .models import Restaurant, Food, FoodOption

class FoodOptionInline(admin.TabularInline):
    model = FoodOption
    fk_name = "food"
    readonly_fields = ('uuid', 'uuid_url', 'food_url')

class FoodInline(admin.TabularInline):
    model = Food
    fk_name = "restaurant"
    readonly_fields = ('uuid', 'uuid_url', 'restaurant_url')

class RestaurantAdmin(admin.ModelAdmin):
    inlines = [
        FoodInline,
    ]
    readonly_fields = ('uuid', 'uuid_url', )

class FoodAdmin(admin.ModelAdmin):
    inlines = [
        FoodOptionInline,
    ]
    readonly_fields = ('uuid', 'uuid_url', 'restaurant_url')

class FoodOptionAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'uuid_url', 'food_url')

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(FoodOption, FoodOptionAdmin)