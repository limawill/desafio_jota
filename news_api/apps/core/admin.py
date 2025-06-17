from django.contrib import admin
from .models import Category, Subcategory, Tag, News

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'description']
    list_filter = ['category']
    search_fields = ['name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'subcategory', 'publication_date', 'is_urgent']
    list_filter = ['category', 'subcategory', 'is_urgent', 'publication_date']
    search_fields = ['title', 'content']
    filter_horizontal = ['tags']

# Register your models here.
