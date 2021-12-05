from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
    path('desk/', include('mmodesk.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),

]
