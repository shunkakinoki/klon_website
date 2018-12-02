from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
from django.views.decorators.csrf import csrf_exempt

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    path('', include('home.urls', namespace="home")),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(('api.urls', 'api'), namespace="api")),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('accounts/', include('allauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)