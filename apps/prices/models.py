import reversion

from .abstracts import AbstractProductChainBase
from .choices import PriceStatusChoice
from .choices import PriceTypeChoice
from apps.commons.models.mixins import SoftControlModel
from apps.product_groups.models import ProductGroup
from apps.product_types.abstracts import AbstracPackagingAttibute
from apps.product_types.abstracts import AbstractCourseAttibute
from apps.product_types.abstracts import AbstractCourseBookAttibute
from apps.product_types.abstracts import AbstractCourseEduGadgetAttibute
from apps.product_types.abstracts import AbstractCourseServiceAttibute
from apps.product_types.abstracts import AbstractEDocumentAttibute
from apps.product_types.abstracts import AbstractEduGadgetAttibute
from apps.product_types.abstracts import AbstractEduGadgetBundleAttibute
from apps.product_types.abstracts import AbstractExternalCourseAttibute
from apps.product_types.abstracts import AbstractExternalExamAttibute
from apps.product_types.abstracts import AbstractFacebookPrivateGroupAttibute
from apps.product_types.abstracts import AbstractGiftAttibute
from apps.product_types.abstracts import AbstractSimulationTestAttibute
from apps.product_types.abstracts import AbstractSupportSaleAttibute
from apps.product_types.choices import ProductTypeChoice
from apps.products.models import Product
from decimal import Decimal
from django.db import models
from django.utils.translation import ugettext_lazy as _


@reversion.register()
class Price(SoftControlModel):

    # Price Info
    code = models.CharField(max_length=255, unique=True, verbose_name=_("Price Code"))
    name = models.CharField(max_length=255, verbose_name=_("Price Name"))
    description = models.TextField(verbose_name=_("Description"))
    price_type = models.PositiveSmallIntegerField(
        choices=PriceTypeChoice.choices,
        default=PriceTypeChoice.FULL_PAYMENT,
        verbose_name=_("Price Type")
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10,  # xx,xxx,xxx.xx --> 0.00 to 99,999,999.99
        verbose_name=_("price")
    )
    reference_product = models.ForeignKey(
        Product,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Reference Product")
    )
    products = models.ManyToManyField(
        Product,
        through='PriceProduct',
        through_fields=('price', 'product'),
        related_name='products',
        verbose_name=_("Products"),
    )
    # Price Status
    price_status = models.PositiveSmallIntegerField(
        choices=PriceStatusChoice.choices,
        default=PriceStatusChoice.DARFT,
        verbose_name=_("Price status")
    )
    
    class Meta:
        verbose_name = _("Price")
        verbose_name_plural = _("Prices")
        ordering = ("pk",)

    def __str__(self):
        return self.code


@reversion.register()
class PriceProduct(SoftControlModel):
    price = models.ForeignKey(
        Price,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Price")
    )
    product = models.ForeignKey(
        Product,
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
        verbose_name = _("Price - Product")
        verbose_name_plural = _("Price - Products")
        ordering = ("pk",)
        unique_together = [
            ("price", "product", "live"),
        ]

    def __str__(self):
        return self.product.name


@reversion.register()
class CourseBookOptional(AbstractProductChainBase, AbstractCourseBookAttibute, SoftControlModel):
    price_product = models.OneToOneField(
        PriceProduct,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Price Product")
    )
    product_chain = models.ForeignKey(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.COURSE_BOOK
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product Chain")
    )

    class Meta:
        verbose_name = _("Course Book Optional")
        verbose_name_plural = _("Course Book Optionals")
        ordering = ("pk",)

    def __str__(self):
        return self.pk


@reversion.register()
class CourseBundleOptional(AbstractProductChainBase, AbstractCourseBookAttibute, SoftControlModel):
    price_product = models.OneToOneField(
        PriceProduct,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Price Product")
    )
    product_chain = models.ForeignKey(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.COURSE_BUNDLE
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product Chain")
    )

    class Meta:
        verbose_name = _("Course Bundle Optional")
        verbose_name_plural = _("Course Bundle Optionals")
        ordering = ("pk",)

    def __str__(self):
        return self.pk


@reversion.register()
class CourseServiceOptional(AbstractProductChainBase, AbstractCourseServiceAttibute, SoftControlModel):
    price_product = models.OneToOneField(
        PriceProduct,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Price Product")
    )
    product_chain = models.ForeignKey(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.COURSE_SERVICE
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product Chain")
    )

    class Meta:
        verbose_name = _("Course Service Optional")
        verbose_name_plural = _("Course Service Optionals")
        ordering = ("pk",)

    def __str__(self):
        return self.pk


@reversion.register()
class CourseOptional(AbstractProductChainBase, AbstractCourseAttibute, SoftControlModel):
    price_product = models.OneToOneField(
        PriceProduct,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Price Product")
    )

    product_chain = models.ForeignKey(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.COURSE
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product Chain")
    )

    class Meta:
        verbose_name = _("Course Optional")
        verbose_name_plural = _("Course Optionals")
        ordering = ("pk",)

    def __str__(self):
        return self.pk


@reversion.register()
class EDocumentOptional(AbstractProductChainBase, AbstractEDocumentAttibute, SoftControlModel):
    price_product = models.OneToOneField(
        PriceProduct,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Price Product")
    )
    product_chain = models.ForeignKey(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.E_DOCUMENT
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product Chain")
    )

    class Meta:
        verbose_name = _("E-Document Optional")
        verbose_name_plural = _("E-Document Optionals")
        ordering = ("pk",)

    def __str__(self):
        return self.pk


@reversion.register()
class EduGadgetBundleOptional(AbstractProductChainBase, AbstractEduGadgetBundleAttibute, SoftControlModel):
    price_product = models.OneToOneField(
        PriceProduct,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Price Product")
    )
    product_chain = models.ForeignKey(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.EDUGADGET_BUNDLE
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product Chain")
    )

    class Meta:
        verbose_name = _("EduGadget Bundle Optional")
        verbose_name_plural = _("EduGadget Bundle Optionals")
        ordering = ("pk",)

    def __str__(self):
        return self.pk


@reversion.register()
class EduGadgetOptional(AbstractProductChainBase, AbstractEduGadgetAttibute, SoftControlModel):
    price_product = models.OneToOneField(
        PriceProduct,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Price Product")
    )
    product_chain = models.ForeignKey(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.EDUGADGET
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product Chain")
    )

    class Meta:
        verbose_name = _("EduGadget Optional")
        verbose_name_plural = _("EduGadget Optionals")
        ordering = ("pk",)

    def __str__(self):
        return self.pk


@reversion.register()
class SimulationTestOptional(AbstractProductChainBase, AbstractSimulationTestAttibute, SoftControlModel):
    price_product = models.OneToOneField(
        PriceProduct,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Price Product")
    )
    product_chain = models.ForeignKey(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.SIMULATION_TEST
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product Chain")
    )

    class Meta:
        verbose_name = _("Simulation Test Optional")
        verbose_name_plural = _("Simulation Test Optionals")
        ordering = ("pk",)

    def __str__(self):
        return self.pk


@reversion.register()
class FacebookPrivateGroupOptional(AbstractProductChainBase, AbstractFacebookPrivateGroupAttibute, SoftControlModel):
    price_product = models.OneToOneField(
        PriceProduct,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Price Product")
    )
    product_chain = models.ForeignKey(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.FACEBOOK_PRIVATE_GROUP
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product Chain")
    )

    class Meta:
        verbose_name = _("Facebook Private Group Optional")
        verbose_name_plural = _("Facebook Private Group Optionals")
        ordering = ("pk",)

    def __str__(self):
        return self.pk


@reversion.register()
class ExternalCourseOptional(AbstractProductChainBase, AbstractExternalCourseAttibute, SoftControlModel):
    price_product = models.OneToOneField(
        PriceProduct,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Price Product")
    )
    product_chain = models.ForeignKey(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.EXTERNAL_CAURSE
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product Chain")
    )

    class Meta:
        verbose_name = _("External Course Optional")
        verbose_name_plural = _("External Course Optionals")
        ordering = ("pk",)

    def __str__(self):
        return self.pk


@reversion.register()
class ExternalExamOptional(AbstractProductChainBase, AbstractExternalExamAttibute, SoftControlModel):
    price_product = models.OneToOneField(
        PriceProduct,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Price Product")
    )
    product_chain = models.ForeignKey(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.EXTERNAL_EXAM
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product Chain")
    )

    class Meta:
        verbose_name = _("External Exam Optional")
        verbose_name_plural = _("External Exam Optionals")
        ordering = ("pk",)

    def __str__(self):
        return self.pk


@reversion.register()
class SupportSaleOptional(AbstractProductChainBase, AbstractSupportSaleAttibute, SoftControlModel):
    price_product = models.OneToOneField(
        PriceProduct,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Price Product")
    )
    product_chain = models.ForeignKey(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.SUPPORT_SALE
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product Chain")
    )

    class Meta:
        verbose_name = _("Support Sale Optional")
        verbose_name_plural = _("Support Sale Optionals")
        ordering = ("pk",)

    def __str__(self):
        return self.pk


@reversion.register()
class PackagingOptional(AbstractProductChainBase, AbstracPackagingAttibute, SoftControlModel):
    price_product = models.OneToOneField(
        PriceProduct,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Price Product")
    )
    product_chain = models.ForeignKey(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.PACKAGING
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product Chain")
    )

    class Meta:
        verbose_name = _("Packaging Optional")
        verbose_name_plural = _("Packaging Optionals")
        ordering = ("pk",)

    def __str__(self):
        return self.pk


@reversion.register()
class CourseEduGadgetOptional(AbstractProductChainBase, AbstractCourseEduGadgetAttibute, SoftControlModel):
    price_product = models.OneToOneField(
        PriceProduct,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Price Product")
    )
    product_chain = models.ForeignKey(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.COURSE_EduGadget
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product Chain")
    )

    class Meta:
        verbose_name = _("Course EduGadget Optional")
        verbose_name_plural = _("Course EduGadget Optionals")
        ordering = ("pk",)

    def __str__(self):
        return self.pk


@reversion.register()
class GiftOptional(AbstractProductChainBase, AbstractGiftAttibute, SoftControlModel):
    price_product = models.OneToOneField(
        PriceProduct,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Price Product")
    )
    product_chain = models.ForeignKey(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.GIFT
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product Chain")
    )

    class Meta:
        verbose_name = _("Gift Optional")
        verbose_name_plural = _("Gift Optionals")
        ordering = ("pk",)

    def __str__(self):
        return self.pk
