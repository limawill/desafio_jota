from django.contrib import admin
from .models import Classification

@admin.register(Classification)
class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('news', 'sentiment', 'relevance_score', 'category', 'created_at')
    list_filter = ('sentiment', 'category')
    search_fields = ('news__title', 'category')