from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        indexes = [models.Index(fields=['name'])]
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    description = models.TextField(blank=True)
    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"
        unique_together = ['name', 'category']
        indexes = [models.Index(fields=['name', 'category'])]
    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        indexes = [models.Index(fields=['name'])]
    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()  # Obrigatório, conforme desafio
    source = models.CharField(max_length=200)  # Obrigatório, conforme desafio
    publication_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='news')
    tags = models.ManyToManyField(Tag, related_name='news', blank=True)  # Agora opcional
    is_urgent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['publication_date']),
            models.Index(fields=['category', 'subcategory']),
        ]
    def __str__(self):
        return self.title