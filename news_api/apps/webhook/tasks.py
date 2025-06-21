from celery import shared_task
from news_api.apps.core.models import Category, Subcategory, Tag, News
from news_api.apps.classification.classifier import classify_news
from news_api.apps.classification.models import Classification

@shared_task
def process_news(data):
    # Obter ou criar a categoria
    category, _ = Category.objects.get_or_create(name=data['category'])

    # Obter ou criar a subcategoria, se fornecida
    subcategory = None
    if data.get('subcategory'):
        subcategory, _ = Subcategory.objects.get_or_create(
            name=data['subcategory'], category=category
        )

    # Obter ou criar tags, se fornecidas
    tags = []
    for tag_name in data.get('tags', []):
        tag, _ = Tag.objects.get_or_create(name=tag_name)
        tags.append(tag)

    # Criar a notícia
    news = News.objects.create(
        title=data['title'],
        content=data['content'],
        source=data['source'],
        publication_date=data['publication_date'],
        category=category,
        subcategory=subcategory,
        is_urgent=data['is_urgent']
    )

    # Associar tags
    if tags:
        news.tags.set(tags)

    # Classificar a notícia
    classification_result = classify_news(data['title'], data['content'], data['category'])
    Classification.objects.create(
        news=news,
        sentiment=classification_result['sentiment'],
        relevance_score=classification_result['relevance_score'],
        category=classification_result['category']
    )

    return news.id