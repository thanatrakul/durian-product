import reversion

from .choices import ProductImageDisplayTypeChoice
from .choices import ProductStatusChoice
from .choices import ProductTaxTypeChoice
from apps.commons.models.mixins import SoftControlModel
from apps.product_groups.models import ProductGroup
from apps.product_types.choices import ProductTypeChoice
from decimal import Decimal
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField


@reversion.register()
class Product(SoftControlModel):

    # Product Info
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_("Slug"))
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))

    # SKU
    sku_code = models.CharField(max_length=20, verbose_name=_("SKU Code"))
    lagacy_sku = models.CharField(max_length=20,default="" , verbose_name=_("Lagacy SKU"))

    # tax
    tax = models.PositiveSmallIntegerField(
        choices=ProductTaxTypeChoice.choices,
        default=ProductTaxTypeChoice.EXCLUDE_VAT,
        verbose_name=_("Tax")
    )

    # Status
    status = models.PositiveSmallIntegerField(
        choices=ProductStatusChoice.choices,
        default=ProductStatusChoice.DRAFT,
        verbose_name=_("Status")
    )

    # Product Type
    product_type = models.PositiveSmallIntegerField(
        choices=ProductTypeChoice.choices,
        default=ProductTypeChoice.COURSE,
        verbose_name=_("Product Type")
    )

    product_group = models.ForeignKey(
        ProductGroup,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product Group")
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ("pk",)

    def __str__(self):
        return self.name


@reversion.register()
class ProductImage(SoftControlModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product")
    )
    image = FilerImageField(
        on_delete=models.DO_NOTHING,
        related_name="product_image",
        verbose_name=_("Image")
    )
    
    description = models.TextField(verbose_name=_("Description"), default="")
    alt_image = models.CharField(max_length=255, verbose_name=_("Alt. Image"))
    display_type = models.PositiveSmallIntegerField(
        choices=ProductImageDisplayTypeChoice.choices,
        default=ProductImageDisplayTypeChoice.DESKTOP
    )

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
        ordering = ("pk",)

    def __str__(self):
        return self.product.name


@reversion.register()
class BundleSet(SoftControlModel):
    name = models.CharField(max_length=255, verbose_name=_("Bundle Set - Name"))
    product = models.ForeignKey(
        Product,
        limit_choices_to={
            'product_type__in': [
                ProductTypeChoice.COURSE,
                ProductTypeChoice.COURSE_BOOK,
                ProductTypeChoice.COURSE_SERVICE,
                ProductTypeChoice.EDUGADGET,
                ProductTypeChoice.SIMULATION_TEST,
                ProductTypeChoice.E_DOCUMENT,
                ProductTypeChoice.COURSE_EduGadget,
                ProductTypeChoice.EXTERNAL_CAURSE,
                ProductTypeChoice.EXTERNAL_EXAM,
                ProductTypeChoice.FACEBOOK_PRIVATE_GROUP,
            ]
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product")
    )
    items = models.ManyToManyField(
        Product,
        through='BundleSetItem',
        through_fields=('bundle_set', 'product'),
        related_name='items',
        verbose_name=_("Products"),
    )

    class Meta:
        app_label = "products"
        verbose_name = _("Bundle Set")
        verbose_name_plural = _("Bundle Sets")
        ordering = ("pk",)
        unique_together = [
            ("name", "product", "live")
        ]

    def __str__(self):
        return self.name


@reversion.register()
class BundleSetItem(SoftControlModel):
    bundle_set = models.ForeignKey(
        BundleSet,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Bundle Set")
    )
    product = models.ForeignKey(
        Product,
        limit_choices_to={
            'product_type__in': [
                ProductTypeChoice.COURSE,
                ProductTypeChoice.COURSE_BOOK,
                ProductTypeChoice.COURSE_SERVICE,
                ProductTypeChoice.EDUGADGET,
                ProductTypeChoice.SIMULATION_TEST,
                ProductTypeChoice.E_DOCUMENT,
                ProductTypeChoice.COURSE_EduGadget,
                ProductTypeChoice.EXTERNAL_CAURSE,
                ProductTypeChoice.EXTERNAL_EXAM,
                ProductTypeChoice.FACEBOOK_PRIVATE_GROUP
            ]
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product")
    )
    quantity = models.DecimalField(
        default=Decimal(1),
        decimal_places=2,
        max_digits=5,  # xxx.xx --> 0.00 to 999.99
        verbose_name=_("Quantity")
    )
    product_group = models.ForeignKey(
        ProductGroup,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product Group")
    )

    class Meta:
        verbose_name = _("Bundle Set - Item")
        verbose_name_plural = _("Bundle Set - Items")
        ordering = ("pk",)
        unique_together = [
            ("bundle_set", "product", "live"),
        ]

    def __str__(self):
        return self.bundle_set.name  # represent data record of table
