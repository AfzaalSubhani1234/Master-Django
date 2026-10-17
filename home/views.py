
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from .serializers import ProductSerializer
from .models import Product


# List all products with ordering
class PostList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [OrderingFilter]
    ordering_fields = ["id", "name", "price"]
    ordering = ["id"]


# Create a product
class PostCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Retrieve a single product by slug
class PostRetrieve(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"


