from django.contrib import admin
from django.urls import path, include

v1_urls = [
    path('v1/', include('apps.authentication.urls')),
    path('v1/', include('apps.links.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(v1_urls)),
    path('', include('public.urls')),
]
