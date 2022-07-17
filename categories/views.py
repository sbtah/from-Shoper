from categories.models import Category
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class CategoryListView(LoginRequiredMixin, generic.ListView):

    model = Category
    context_object_name = "categories"
    template_name = "categories/categories_list.html"


class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    """DetailView for Product object."""

    model = Category
    template_name = "categories/category_detail.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        """Get data about Products and CategoryTranslations related to this object."""

        context = super().get_context_data(**kwargs)

        category = kwargs.get("object")
        context["related_products"] = category.shoper_products.all()
        context["related_translations"] = category.categorytranslation_set.all()

        return context
