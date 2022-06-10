from apps.commons.api.mixins import CRUDSerializerMixin
from apps.products.models import BundleSet
from apps.products.models import BundleSetItem
from apps.products.models import Product
from apps.products.models import ProductImage


class ProductSerializer(CRUDSerializerMixin):

    class Meta:
        model = Product
        fields = [
            "id",
            "slug",
            "name",
            "sku_code",
            "lagacy_sku",
            "tax",
            "status",
            "product_type",
            "product_group",
            "live",
        ]


class ProductImageSerializer(CRUDSerializerMixin):

    class Meta:
        model = ProductImage
        fields = [
            "id",
            "product",
            "image",
            'description',
            "alt_image",
            "display_type",
            "live"
        ]


class BundleSetSerializer(CRUDSerializerMixin):
    class Meta:
        model = BundleSet
        fields = [
            "id",
            "name",
            "product",
            "items",
            "live",
        ]


class BundleSetItemSerializer(CRUDSerializerMixin):
    class Meta:
        model = BundleSetItem
        fields = [
            "id",
            "bundle_set",
            "product",
            "quantity",
            "live",
        ]
