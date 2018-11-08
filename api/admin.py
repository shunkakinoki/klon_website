from django.contrib import admin

from .models import Restaurant, Food, FoodOption

class RestaurantAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'uuid_url')

class FoodAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'uuid_url')

class FoodOptionAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(FoodOption, FoodOptionAdmin)