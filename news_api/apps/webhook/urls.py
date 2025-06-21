from django.urls import path
from .views import NewsWebhookView

urlpatterns = [
    path('news/', NewsWebhookView.as_view(), name='news-webhook'),
]