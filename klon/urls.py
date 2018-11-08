from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
import rest_framework

urlpatterns = [
    path('', include('home.urls', namespace="home")),
    path('admin/', admin.site.urls),
    path('api/', include(('api.urls', 'api'), namespace="api")),
    path('api-auth/', include(('rest_framework.urls', 'api-auth'), namespace="api-auth")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)