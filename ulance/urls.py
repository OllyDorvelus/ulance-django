"""ulance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('api/accounts/', include('accounts.api.urls')),
    path('', include('accounts.urls')),
    path('', include('profiles.urls')),
    path('api/profiles/', include('profiles.api.urls')),
    path('', include('services.urls')),
    path('api/services', include('services.api.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/auth/token', obtain_jwt_token),
    path('rest-auth/', include('rest_auth.urls')),

]


if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

