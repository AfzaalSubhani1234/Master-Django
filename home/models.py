
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    choices = [
        ('fashion', 'Fashion'),
        ('IT', 'IT'),
        ('electronics', 'Electronics'),
        ('sports', 'Sports'),
        ('books', 'Books'),
        ('health', 'Health'),
        ('beauty', 'Beauty'),
        ('food', 'Food'),
        ('education', 'Education'),
        ('technology', 'Technology'),
    ]

    name = models.CharField(
        max_length=120,
        choices=choices
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='products'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    Title=models.CharField(max_length=500)
    description = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=500, unique=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.description[:50]

