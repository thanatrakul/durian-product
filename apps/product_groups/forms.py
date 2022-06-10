from .models import ProductGroup
from apps.commons.forms.mixins import SoftControlControlModelFormMixin


class ProductGroupForm(SoftControlControlModelFormMixin):
    class Meta:
        model = ProductGroup
        fields = [
            "name",
            "lms_id",
            "slug",
            "live"
        ]
