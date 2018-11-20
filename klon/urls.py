from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
    path('', include('home.urls', namespace="home")),
    url(r'^', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(('api.urls', 'api'), namespace="api")),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('rest_auth.urls')),
    path('auth/register/', include('rest_auth.registration.urls')),
    # path('accounts/', include('allauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)