from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


from .models import Restaurant, Food, FoodOption, UserProfile


class FoodOptionInline(admin.TabularInline):
    model = FoodOption
    fk_name = "food"
    exclude = ('uuid', 'uuid_admin', 'uuid_url', 'food_admin', 'food_url',)
    readonly_fields = ('foodoption_admin_link',)

    def foodoption_admin_link(self, instance):
        return format_html('<a href="{url}" target=_blank>{url}</a>', url=instance.uuid_admin)


class FoodInline(admin.TabularInline):
    model = Food
    fk_name = "restaurant"
    exclude = ('uuid', 'uuid_admin', 'uuid_url', 'restaurant_admin', 'restaurant_url',)
    readonly_fields = ('food_admin_link',)

    def food_admin_link(self, instance):
        return format_html('<a href="{url}" target=_blank>{url}</a>', url=instance.uuid_admin)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


class RestaurantAdmin(admin.ModelAdmin):
    inlines = [
        FoodInline,
    ]
    readonly_fields = ('uuid', 'uuid_url', )


class FoodAdmin(admin.ModelAdmin):
    inlines = [
        FoodOptionInline,
    ]
    exclude = ('uuid', 'uuid_admin', 'uuid_url', 'restaurant_admin', 'restaurant_url',)
    list_display = ('name', 'restaurant', 'restaurant_admin_link',)
    list_display_links = ('name', 'restaurant_admin_link',)
    readonly_fields = ('restaurant_admin_link',)

    def restaurant_admin_link(self, instance):
        return format_html('<a href="{url}" target=_blank>{url}</a>', url=instance.restaurant_admin)


class FoodOptionAdmin(admin.ModelAdmin):
    exclude = ('uuid', 'uuid_admin', 'uuid_url', 'food_admin', 'food_url',)
    list_display = ('name', 'food', 'food_admin_link', )
    list_display_links = ('name', 'food_admin_link', )
    readonly_fields = ('food_admin_link',)

    def food_admin_link(self, instance):
        return format_html('<a href="{url}" target=_blank>{url}</a>', url=instance.food_admin)


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(FoodOption, FoodOptionAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)