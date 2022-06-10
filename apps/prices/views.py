from .forms import PriceForm
from .models import Price
from apps.commons.views.mixins import CreateControlModelViewMixin
from apps.commons.views.mixins import DeleteControlModelViewMixin
from apps.commons.views.mixins import UpdateControlModelViewMixin
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class PriceBaseView(object):
    model = Price
    form_class = PriceForm


class PriceListView(PriceBaseView, ListView):
    template_name = "prices/list.html"


class PriceCreateView(PriceBaseView, CreateControlModelViewMixin):
    template_name = "prices/form.html"

    def get_success_url(self):
        return reverse('prices:detail', kwargs={
            'pk': self.object.pk,
        })


class PriceUpdateView(PriceBaseView, UpdateControlModelViewMixin):
    template_name = "prices/form.html"

    def get_success_url(self):
        return reverse('prices:detail', kwargs={
            'pk': self.object.pk,
        })


class PriceDeleteView(PriceBaseView, DeleteControlModelViewMixin):
    template_name = "prices/confirm_delete.html"

    def get_success_url(self):
        return reverse('prices:all')


class PriceDetailView(PriceBaseView, DetailView):
    template_name = "prices/detail.html"
