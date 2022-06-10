from apps.commons.api.mixins import CRUDSerializerMixin
from apps.product_groups.models import ProductGroup


class ProductGroupSerializer(CRUDSerializerMixin):

    class Meta:
        model = ProductGroup
        fields = [
            "id",
            "name",
            "lms_id",
            "slug",
            "live"
        ]
