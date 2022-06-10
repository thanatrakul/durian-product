from apps.commons.api.mixins import CRUDSerializerMixin
from apps.costs.models import ProductCost


class ProductCostSerializer(CRUDSerializerMixin):

    class Meta:
        model = ProductCost
        fields = [
            "id",
            "product",
            "cost",
            "mms_timestamp",
            "live"
        ]
