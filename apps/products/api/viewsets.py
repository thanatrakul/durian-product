from apps.commons.api.viewsets import CRUDViewsetMixin
from apps.products.api.serializers import BundleSetItemSerializer
from apps.products.api.serializers import BundleSetSerializer
from apps.products.api.serializers import ProductImageSerializer
from apps.products.api.serializers import ProductSerializer
from apps.products.models import BundleSet
from apps.products.models import BundleSetItem
from apps.products.models import Product
from apps.products.models import ProductImage


class ProductViewSet(CRUDViewsetMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductImageItemViewSet(CRUDViewsetMixin):
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()


class BundleSetViewSet(CRUDViewsetMixin):
    serializer_class = BundleSetSerializer
    queryset = BundleSet.objects.all()


class BundleSetItemViewSet(CRUDViewsetMixin):
    serializer_class = BundleSetItemSerializer
    queryset = BundleSetItem.objects.all()
