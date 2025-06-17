from rest_framework import serializers
from news_api.apps.core.models import Category, Subcategory, Tag, News

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
        # Obter ou criar a categoria
        category, _ = Category.objects.get_or_create(name=validated_data['category'])

        # Obter ou criar a subcategoria, se fornecida
        subcategory = None
        if validated_data.get('subcategory'):
            subcategory, _ = Subcategory.objects.get_or_create(
                name=validated_data['subcategory'], category=category
            )

        # Obter ou criar tags, se fornecidas
        tags = []
        for tag_name in validated_data.get('tags', []):
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tags.append(tag)

        # Criar a notícia
        news = News.objects.create(
            title=validated_data['title'],
            content=validated_data['content'],
            source=validated_data['source'],
            publication_date=validated_data['publication_date'],
            category=category,
            subcategory=subcategory,
            is_urgent=validated_data['is_urgent']
        )

        # Associar tags à notícia
        if tags:
            news.tags.set(tags)

        return news
