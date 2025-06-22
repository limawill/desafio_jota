from django.contrib import admin
from .models import News, Category, Subcategory, Tag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']  # Removido 'description'
    search_fields = ['name']

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name']  # Removido 'category' e 'description'
    list_filter = []  # Removido 'category'
    search_fields = ['name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'source', 'publication_date', 'category', 'is_urgent']
    list_filter = ['category', 'subcategory', 'is_urgent']
    search_fields = ['title', 'content']
