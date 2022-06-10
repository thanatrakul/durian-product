from .forms import ProductForm
from .models import Product
from apps.commons.views.mixins import CreateControlModelViewMixin
from apps.commons.views.mixins import DeleteControlModelViewMixin
from apps.commons.views.mixins import UpdateControlModelViewMixin
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class ProductBaseView(object):
    model = Product
    form_class = ProductForm


class ProductListView(ProductBaseView, ListView):
    template_name = "products/list.html"


class ProductCreateView(ProductBaseView, CreateControlModelViewMixin):
    template_name = "products/form.html"

    def get_success_url(self):
        return reverse('products:detail', kwargs={
            'pk': self.object.pk,
        })


class ProductUpdateView(ProductBaseView, UpdateControlModelViewMixin):
    template_name = "products/form.html"

    def get_success_url(self):
        return reverse('products:detail', kwargs={
            'pk': self.object.pk,
        })


class ProductDeleteView(ProductBaseView, DeleteControlModelViewMixin):
    template_name = "products/confirm_delete.html"

    def get_success_url(self):
        return reverse('products:all')


class ProductDetailView(ProductBaseView, DetailView):
    template_name = "products/detail.html"
