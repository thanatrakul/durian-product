from .models import BundleSet
from .models import BundleSetItem
from .models import Product
from .models import ProductImage
from apps.commons.forms.mixins import SoftControlControlModelFormMixin


class ProductImageForm(SoftControlControlModelFormMixin):

    class Meta:
        model = ProductImage
        fields = [
            "product",
            "image",
            "alt_image",
            "display_type",
            "live"
        ]


class ProductForm(SoftControlControlModelFormMixin):

    class Meta:
        model = Product
        fields = [
            "slug",
            "name",
            "description",
            "sku_code",
            "lagacy_sku",
            "tax",
            "status",
            "product_type",
            "product_group",
            "live"
        ]


class BundleSetForm(SoftControlControlModelFormMixin):
    class Meta:
        model = BundleSet
        fields = [
            "name",
            "product",
            "items",
            "live"
        ]


class BundleSetItemForm(SoftControlControlModelFormMixin):
    class Meta:
        model = BundleSetItem
        fields = [
            "bundle_set",
            "product",
            "quantity",
            "product_group",
            "live"
        ]
