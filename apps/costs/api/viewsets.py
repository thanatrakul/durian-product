from apps.commons.api.viewsets import CRUDViewsetMixin
from apps.costs.api.serializers import ProductCostSerializer
from apps.costs.models import ProductCost


class ProductCostViewSet(CRUDViewsetMixin):
    serializer_class = ProductCostSerializer
    queryset = ProductCost.objects.all()
