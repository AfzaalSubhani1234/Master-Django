from django.urls import path
from .views import PostList, PostCreate, PostRetrieve

urlpatterns = [
    path(
        "products/",
        PostList.as_view(),
        name="product-list",
    ),
    path(
        "products/create/",
        PostCreate.as_view(),
        name="product-create",
    ),
    path(
        "products/<slug:slug>/",
        PostRetrieve.as_view(),
        name="product-detail",
    ),
]
