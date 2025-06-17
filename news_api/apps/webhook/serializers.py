from rest_framework import serializers
from .tasks import process_news

class NewsWebhookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    source = serializers.CharField(max_length=200)
    publication_date = serializers.DateTimeField()
    category = serializers.CharField(max_length=100)
    subcategory = serializers.CharField(max_length=100, required=False, allow_null=True)
    tags = serializers.ListField(child=serializers.CharField(max_length=50), required=False, allow_empty=True)
    is_urgent = serializers.BooleanField(default=False)

    def create(self, validated_data):
        # Enviar dados para a fila via Celery
        process_news.delay(validated_data)
        return validated_data