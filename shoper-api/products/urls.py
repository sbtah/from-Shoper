from django.urls import path
from products.views import (
    ProductListView,
    ProductDetailView,
    ProductUpdateFromShoperView,
)


app_name = "products"


urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path(
        "update-to-shoper/<int:pk>/",
        ProductUpdateFromShoperView.as_view(),
        name="product-from-shoper-update",
    ),
]
