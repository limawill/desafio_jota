from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from news_api.apps.core.models import News
from news_api.apps.api.serializers import NewsSerializer

class NewsListView(generics.ListAPIView):
    queryset = News.objects.select_related('category', 'subcategory').prefetch_related('tags', 'classifications')
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [
        'is_urgent',
        'category__name',
        'classifications__sentiment',
        'publication_date',
        'tags__name',  # Adicionado
    ]
    search_fields = ['title', 'content']
    ordering_fields = ['publication_date', 'classifications__relevance_score']
    ordering = ['-publication_date']