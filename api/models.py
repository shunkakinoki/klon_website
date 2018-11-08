from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField
import uuid

WEEKDAYS = [
  (1, ("Monday")),
  (2, ("Tuesday")),
  (3, ("Wednesday")),
  (4, ("Thursday")),
  (5, ("Friday")),
  (6, ("Saturday")),
  (7, ("Sunday")),
]

class Restaurant(models.Model):
    """
    The base model class for restaurant
    """

    def restaurant_image_path(instance, filename):
        return 'image/restaurant/{0}/{1}'.format(instance.uuid, filename)

    def restaurant_file_path(instance, filename):
        return 'file/restaurant/{0}/{1}'.format(instance.uuid, filename)

    uuid             = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    uuid_url         = models.URLField(max_length=200, null=True, blank=True)
    name             = models.CharField(max_length=128)
    created_date     = models.DateField(auto_now_add=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    
    homepage_urllink = models.URLField(max_length=200, null=True, blank=True)
    rating           = models.PositiveSmallIntegerField(null=True, blank=True)
    description      = models.CharField(max_length=512, null=True, blank=True)
    features         = models.CharField(max_length=128, null=True, blank=True)
    cuisine          = models.CharField(max_length=128, null=True, blank=True)
    email            = models.EmailField(max_length=128, null=True, blank=True)
    phone            = models.CharField(max_length=40, null=True, blank=True)
    address          = models.CharField(max_length=256, null=True, blank=True)
    post_code        = models.CharField(max_length=20, null=True, blank=True) 

    image_1          = models.ImageField(upload_to=restaurant_image_path, null=True, blank=True)
    image_2          = models.ImageField(upload_to=restaurant_image_path, null=True, blank=True)
    image_3          = models.ImageField(upload_to=restaurant_image_path, null=True, blank=True)
    video            = models.FileField(upload_to=restaurant_file_path, null=True, blank=True)
    video_urllink    = models.URLField(max_length=200, null=True, blank=True)

    open_day         = MultiSelectField(
        choices=WEEKDAYS,
        unique=True,
        max_choices=7,
        max_length=7,
        null=True,
        blank=True
    )
    open_from_hour   = models.TimeField(null=True, blank=True)
    open_to_hour     = models.TimeField(null=True, blank=True)

    place_urllink    = models.URLField(max_length=200, null=True, blank=True)
    longitude        = models.DecimalField(
        max_digits=20,
        decimal_places=12, 
        null=True, 
        blank=True
    )
    latitude         = models.DecimalField(
        max_digits=20,
        decimal_places=12, 
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        uuid = self.uuid 
        self.uuid_url = "http://klongroup.com/api/restaurants/" + str(uuid)
        super(Restaurant, self).save(*args, **kwargs)


class Food(models.Model):
    """
    The model class for food
    """

    def food_image_path(instance, filename):
        return 'image/food/{0}/{1}'.format(instance.uuid, filename)

    def food_file_path(instance, filename):
        return 'file/food/{0}/{1}'.format(instance.uuid, filename)

    uuid             = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    uuid_url         = models.URLField(max_length=200, null=True, blank=True)
    restaurant       = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_foods')
    name             = models.CharField(max_length=128)
    created_date     = models.DateField(auto_now_add=True)
    created_datetime = models.DateTimeField(auto_now_add=True)

    rating           = models.PositiveSmallIntegerField(null=True, blank=True)
    description      = models.CharField(max_length=512, null=True, blank=True)
    features         = models.CharField(max_length=128, null=True, blank=True)
    cuisine          = models.CharField(max_length=128, null=True, blank=True)

    price            = models.PositiveIntegerField(null=True, blank=True)
    number           = models.PositiveSmallIntegerField(null=True, blank=True)
    boolean          = models.BooleanField(null=True, blank=True)

    image_1          = models.ImageField(upload_to=food_image_path, null=True, blank=True)
    image_2          = models.ImageField(upload_to=food_image_path, null=True, blank=True)
    image_3          = models.ImageField(upload_to=food_image_path, null=True, blank=True)
    video            = models.FileField(upload_to=food_file_path, null=True, blank=True)
    video_urllink    = models.URLField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        uuid = self.uuid 
        self.uuid_url = "http://klongroup.com/api/foods/" + str(uuid)
        super(Food, self).save(*args, **kwargs)


class FoodOption(models.Model):
    """
    The model class for food option
    """

    def foodoption_image_path(instance, filename):
        return 'image/foodoption/{0}/{1}'.format(instance.uuid, filename)
    
    def foodoption_file_path(instance, filename):
        return 'file/foodoption/{0}/{1}'.format(instance.uuid, filename)

    uuid             = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    food             = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='food_foodoptions')
    name             = models.CharField(max_length=128)
    created_date     = models.DateField(auto_now_add=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    
    description      = models.CharField(max_length=512, null=True, blank=True)

    price            = models.PositiveIntegerField(null=True, blank=True)
    number           = models.PositiveSmallIntegerField(null=True, blank=True)
    boolean          = models.BooleanField(null=True, blank=True)

    image_1          = models.ImageField(upload_to=foodoption_image_path, null=True, blank=True)
    image_2          = models.ImageField(upload_to=foodoption_image_path, null=True, blank=True)
    image_3          = models.ImageField(upload_to=foodoption_image_path, null=True, blank=True)
    video            = models.FileField(upload_to=foodoption_file_path, null=True, blank=True)
    video_urllink    = models.URLField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name