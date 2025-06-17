from django.urls import path
from .views import NewsWebhookView

urlpatterns = [
    path('webhook/news/', NewsWebhookView.as_view(), name='news-webhook'),
]
