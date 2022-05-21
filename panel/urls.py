from django.urls import path
from panel import views
from products.views import (
    ProductListView,
    ProductDetailView,
    ProductUpdateFromShoperView,
)


app_name = "panel"


urlpatterns = [
    path("", views.PanelView.as_view(), name="panel"),
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("images/", views.ImageListView.as_view(), name="image-list"),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path(
        "products/<int:pk>/update/",
        ProductUpdateFromShoperView.as_view(),
        name="product-from-shoper-update",
    ),
]
