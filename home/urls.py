
from django.urls import path
from .views import (
    PostList,
    PostCreate,
    PostRetrieve,
    RegisterView,
)

urlpatterns = [
    path("products/", PostList.as_view(), name="product-list"),
    path("products/create/", PostCreate.as_view(), name="product-create"),
    path(
        "products/<slug:slug>/",
        PostRetrieve.as_view(),
        name="product-detail",
    ),
    path("register/", RegisterView.as_view(), name="register"),
]


