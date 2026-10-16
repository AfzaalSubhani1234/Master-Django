
from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'category',
        'slug',
        'is_published',
        'created_at',
    )
    list_filter = ('is_published', 'category', 'created_at')
    search_fields = ('description', 'slug', 'user__username')
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('Title',)}
    readonly_fields = ('created_at',)
