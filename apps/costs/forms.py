from apps.commons.forms.mixins import SoftControlControlModelFormMixin
from .models import ProductCost


class ProductCostForm(SoftControlControlModelFormMixin):
    class Meta:
        model = ProductCost
        fields = [
            "product",
            "cost",
            "live"
        ]
