from celery import shared_task
from news_api.apps.core.models import Category, Subcategory, Tag, News

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

    # Associar tags à notícia
    if tags:
        news.tags.set(tags)

    return news.id
