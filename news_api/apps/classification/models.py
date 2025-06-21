from django.db import models
from news_api.apps.core.models import News

class Classification(models.Model):
    SENTIMENT_CHOICES = (
        ('POS', 'Positivo'),
        ('NEG', 'Negativo'),
        ('NEU', 'Neutro'),
    )

    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='classifications')
    sentiment = models.CharField(max_length=3, choices=SENTIMENT_CHOICES)
    relevance_score = models.FloatField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.news.title} - {self.get_sentiment_display()} ({self.relevance_score}%)"