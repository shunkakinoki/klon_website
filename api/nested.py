from django.contrib import admin
import nested_admin

from .models import Restaurant, Food, FoodOption

class NestedFoodOptionInline(nested_admin.NestedStackedInline):
    model = FoodOption
    sortable_field_name = "name"

class NestedFoodInline(nested_admin.NestedStackedInline):
    model = Restaurant
    sortable_field_name = "name"
    inlines = [NestedFoodOptionInline]

class NestedRestaurantAdmin(nested_admin.NestedModelAdmin):
    inlines = [NestedFoodInline]

admin.site.register(Restaurant, NestedRestaurantAdmin)
