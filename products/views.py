from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from products.models import Product


class ProductListView(LoginRequiredMixin, generic.ListView):

    model = Product
    context_object_name = "products"
    paginate_by = 10
    template_name = "products/product_list.html"


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    """DetailView for Product object."""

    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    """UpdateView for Product object."""

    pass


class ProductUpdateFromShoperView(LoginRequiredMixin, generic.UpdateView):
    """UpdateView for Product object that pulls data from Shoper API."""

    model = Product

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        print("==================", self.object.shoper_id)
        return super().get(request, *args, **kwargs)
