from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhook/', include('news_api.apps.webhook.urls')),  # Corrigido
    path('api/', include('news_api.apps.api.urls')),
]