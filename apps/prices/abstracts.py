from .choices import ProductChainTypeChoice
from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractProductChainBase(models.Model):

    # Product Chain
    product_chain_type = models.PositiveSmallIntegerField(
        choices=ProductChainTypeChoice.choices,
        default=ProductChainTypeChoice.DO_NOTHING,
        verbose_name=_("Product Chain Type")
    )

    class Meta:
        abstract = True
