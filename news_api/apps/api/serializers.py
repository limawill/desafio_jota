from rest_framework import serializers
from news_api.apps.core.models import News, Category, Subcategory, Tag
from news_api.apps.classification.models import Classification

class ClassificationSerializer(serializers.ModelSerializer):
    sentiment = serializers.CharField(source='get_sentiment_display')

    class Meta:
        model = Classification
        fields = ['sentiment', 'relevance_score', 'category']

class NewsSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    subcategory = serializers.CharField(source='subcategory.name', allow_null=True)
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    classifications = ClassificationSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = [
            'id', 'title', 'content', 'source', 'publication_date',
            'category', 'subcategory', 'tags', 'is_urgent', 'classifications'
        ]
