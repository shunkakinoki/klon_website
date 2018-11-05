from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('home.urls', namespace="home")),
    path('admin/', admin.site.urls),
]
