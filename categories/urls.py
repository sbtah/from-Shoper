from django.urls import path
from categories.views import CategoryListView, CategoryDetailView


app_name = "categories"


urlpatterns = [
    path("", CategoryListView.as_view(), name="categories-list"),
    path("<int:pk>", CategoryDetailView.as_view(), name="category-detail"),
]
