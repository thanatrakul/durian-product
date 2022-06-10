from apps.commons.api.viewsets import CRUDViewsetMixin
from apps.product_groups.api.serializers import ProductGroupSerializer
from apps.product_groups.models import ProductGroup


class ProductGroupViewSet(CRUDViewsetMixin):
    serializer_class = ProductGroupSerializer
    queryset = ProductGroup.objects.all()
