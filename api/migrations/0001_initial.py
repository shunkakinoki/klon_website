# Generated by Django 2.1.3 on 2018-11-07 08:25

import api.models
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('rating', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('features', models.CharField(blank=True, max_length=128, null=True)),
                ('cuisine', models.CharField(blank=True, max_length=128, null=True)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('boolean', models.BooleanField(blank=True, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to=api.models.Food.food_image_path)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to=api.models.Food.food_image_path)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to=api.models.Food.food_image_path)),
                ('video', models.FileField(blank=True, null=True, upload_to=api.models.Food.food_file_path)),
                ('video_urllink', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodOption',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('boolean', models.BooleanField(blank=True, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to=api.models.FoodOption.foodoption_image_path)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to=api.models.FoodOption.foodoption_image_path)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to=api.models.FoodOption.foodoption_image_path)),
                ('video', models.FileField(blank=True, null=True, upload_to=api.models.FoodOption.foodoption_file_path)),
                ('video_urllink', models.URLField(blank=True, null=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Food')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('homepage_urllink', models.URLField(blank=True, null=True)),
                ('rating', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('features', models.CharField(blank=True, max_length=128, null=True)),
                ('cuisine', models.CharField(blank=True, max_length=128, null=True)),
                ('email', models.EmailField(blank=True, max_length=128, null=True)),
                ('phone', models.CharField(blank=True, max_length=40, null=True)),
                ('address', models.CharField(blank=True, max_length=256, null=True)),
                ('post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to=api.models.Restaurant.restaurant_image_path)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to=api.models.Restaurant.restaurant_image_path)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to=api.models.Restaurant.restaurant_image_path)),
                ('video', models.FileField(blank=True, null=True, upload_to=api.models.Restaurant.restaurant_file_path)),
                ('video_urllink', models.URLField(blank=True, null=True)),
                ('open_day', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], max_length=7, null=True, unique=True)),
                ('open_from_hour', models.TimeField(blank=True, null=True)),
                ('open_to_hour', models.TimeField(blank=True, null=True)),
                ('place_urllink', models.URLField(blank=True, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=12, max_digits=20, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=12, max_digits=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Restaurant'),
        ),
    ]