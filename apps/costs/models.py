import reversion
from decimal import Decimal
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.commons.models.mixins import SoftControlModel
from apps.products.models import Product


@reversion.register()
class ProductCost(SoftControlModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product")
    )
    cost = models.DecimalField(
        default=Decimal(1),
        decimal_places=2,
        max_digits=5,  # xxx.xx --> 0.00 to 999.99
        verbose_name=_("cost")
    )
    mms_timestamp = models.DateTimeField(
        verbose_name=_("MMS Timestamp")
    )

    class Meta:
        verbose_name = _("Product Cost")
        verbose_name_plural = _("Product Costs")
        ordering = ("pk",)
        unique_together = [
            ("product", "mms_timestamp", "cost", "live")
        ]
