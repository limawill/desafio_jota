from celery import shared_task
from news_api.apps.core.models import News, Category, Subcategory, Tag
from news_api.apps.classification.models import Classification
import spacy
from django.utils import timezone

# Carregar o modelo spaCy uma vez no início
nlp = spacy.load('pt_core_news_lg')

@shared_task
def process_news(data):
    # Extrair e processar dados
    category, _ = Category.objects.get_or_create(name=data['category'])
    subcategory = Subcategory.objects.get_or_create(name=data.get('subcategory'))[0] if data.get('subcategory') else None
    news = News.objects.create(
        title=data['title'],
        content=data['content'],
        source=data['source'],
        publication_date=data['publication_date'],
        category=category,
        subcategory=subcategory,
        is_urgent=data.get('is_urgent', False),
        created_at=timezone.now()
    )

    # Tags estáticas do payload
    static_tags = data.get('tags', [])
    for tag_name in static_tags:
        tag, _ = Tag.objects.get_or_create(name=tag_name.lower())
        news.tags.add(tag)
        print(f"Tag estática adicionada: {tag_name.lower()}")

    # Extrair tags dinâmicas com spaCy
    doc = nlp(data['content'])
    dynamic_tags = []
    for ent in doc.ents:
        if ent.label_ in ['LOC', 'GPE', 'ORG', 'PERSON']:
            dynamic_tags.append(ent.text.lower())
            print(f"Entidade encontrada: {ent.text} ({ent.label_})")
    for token in doc:
        if token.pos_ == 'NOUN' and token.text.lower() not in dynamic_tags:
            dynamic_tags.append(token.text.lower())
            print(f"Substantivo encontrado: {token.text}")
    dynamic_tags = list(set(dynamic_tags))[:5]
    for tag_name in dynamic_tags:
        tag, _ = Tag.objects.get_or_create(name=tag_name)
        news.tags.add(tag)
        print(f"Tag dinâmica adicionada: {tag_name}")

    # Salvar alterações
    news.save()
    print(f"Notícia salva: ID {news.id}, Tags: {[tag.name for tag in news.tags.all()]}")

    # Simular classificação
    sentiment = 'NEU'
    relevance_score = 38.46153846153847
    Classification.objects.create(
        news=news,
        sentiment=sentiment,
        relevance_score=relevance_score,
        category=data['category']
    )
    print(f"Classificação criada para notícia ID {news.id}")
