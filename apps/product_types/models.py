import reversion

from .abstracts import AbstracPackagingAttibute
from .abstracts import AbstractCourseAttibute
from .abstracts import AbstractCourseBookAttibute
from .abstracts import AbstractCourseBundleAttibute
from .abstracts import AbstractCourseEduGadgetAttibute
from .abstracts import AbstractCourseServiceAttibute
from .abstracts import AbstractEDocumentAttibute
from .abstracts import AbstractEduGadgetAttibute
from .abstracts import AbstractEduGadgetBundleAttibute
from .abstracts import AbstractExternalCourseAttibute
from .abstracts import AbstractExternalExamAttibute
from .abstracts import AbstractFacebookPrivateGroupAttibute
from .abstracts import AbstractGiftAttibute
from .abstracts import AbstractSimulationTestAttibute
from .abstracts import AbstractSupportSaleAttibute
from apps.commons.models.mixins import SoftControlModel
from apps.product_types.choices import ProductTypeChoice
from apps.products.models import Product
from django.db import models
from django.utils.translation import ugettext_lazy as _


@reversion.register()
class CourseBook(AbstractCourseBookAttibute, SoftControlModel):
    product = models.OneToOneField(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.COURSE_BOOK
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product")
    )

    # Inheritance from .abstracts

    class Meta:
        verbose_name = _("Course Book")
        verbose_name_plural = _("Course Books")
        ordering = ("pk",)

    def __str__(self):
        return self.product.name


@reversion.register()
class CourseBundle(AbstractCourseBundleAttibute, SoftControlModel):
    product = models.OneToOneField(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.COURSE_BUNDLE
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product")
    )

    # Inheritance from .abstracts

    class Meta:
        verbose_name = _("Course Bundle")
        verbose_name_plural = _("Course Bundles")
        ordering = ("pk",)

    def __str__(self):
        return self.product.name


@reversion.register()
class CourseService(AbstractCourseServiceAttibute, SoftControlModel):
    product = models.OneToOneField(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.COURSE_SERVICE
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product")
    )

    # Inheritance from .abstracts

    class Meta:
        verbose_name = _("Course Service")
        verbose_name_plural = _("Course Services")
        ordering = ("pk",)

    def __str__(self):
        return self.product.name


@reversion.register()
class Course(AbstractCourseAttibute, SoftControlModel):
    product = models.OneToOneField(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.COURSE
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product")
    )

    # Inheritance from .abstracts

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")
        ordering = ("pk",)

    def __str__(self):
        return self.product.name


@reversion.register()
class EDocument(AbstractEDocumentAttibute, SoftControlModel):
    product = models.OneToOneField(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.E_DOCUMENT
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product")
    )

    # Inheritance from .abstracts

    class Meta:
        verbose_name = _("EDocument")
        verbose_name_plural = _("EDocuments")
        ordering = ("pk",)

    def __str__(self):
        return self.product.name


@reversion.register()
class EduGadgetBundle(AbstractEduGadgetBundleAttibute, SoftControlModel):
    product = models.OneToOneField(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.EDUGADGET_BUNDLE
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product")
    )

    # Inheritance from .abstracts

    class Meta:
        verbose_name = _("EduGadget Bundle")
        verbose_name_plural = _("EduGadget Bundles")
        ordering = ("pk",)

    def __str__(self):
        return self.product.name


@reversion.register()
class EduGadget(AbstractEduGadgetAttibute, SoftControlModel):
    product = models.OneToOneField(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.EDUGADGET
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product")
    )

    # Inheritance from .abstracts

    class Meta:
        verbose_name = _("EduGadget")
        verbose_name_plural = _("EduGadgets")
        ordering = ("pk",)

    def __str__(self):
        return self.product.name


@reversion.register()
class SimulationTest(AbstractSimulationTestAttibute, SoftControlModel):
    product = models.OneToOneField(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.SIMULATION_TEST
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product")
    )

    # Inheritance from .abstracts

    class Meta:
        verbose_name = _("Simulation Test")
        verbose_name_plural = _("Simulation Tests")
        ordering = ("pk",)

    def __str__(self):
        return self.product.name


@reversion.register()
class Packaging(AbstracPackagingAttibute, SoftControlModel):
    product = models.OneToOneField(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.PACKAGING
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product")
    )

    # Inheritance from .abstracts

    class Meta:
        verbose_name = _("Packaging")
        verbose_name_plural = _("Packaging")
        ordering = ("pk",)

    def __str__(self):
        return self.product.name


@reversion.register()
class CourseEduGadget(AbstractCourseEduGadgetAttibute, SoftControlModel):
    product = models.OneToOneField(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.COURSE_EduGadget
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product")
    )

    # Inheritance from .abstracts

    class Meta:
        verbose_name = _("Course EdugGadget")
        verbose_name_plural = _("Course EdugGadgets")
        ordering = ("pk",)

    def __str__(self):
        return self.product.name


@reversion.register()
class ExternalCourse(AbstractExternalCourseAttibute, SoftControlModel):
    product = models.OneToOneField(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.EXTERNAL_CAURSE
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product")
    )

    # Inheritance from .abstracts

    class Meta:
        verbose_name = _("External Course")
        verbose_name_plural = _("External Courses")
        ordering = ("pk",)

    def __str__(self):
        return self.product.name


@reversion.register()
class ExternalExam(AbstractExternalExamAttibute, SoftControlModel):
    product = models.OneToOneField(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.EXTERNAL_EXAM
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product")
    )

    # Inheritance from .abstracts

    class Meta:
        verbose_name = _("External Exam")
        verbose_name_plural = _("External Exams")
        ordering = ("pk",)

    def __str__(self):
        return self.product.name


@reversion.register()
class FacebookPrivateGroup(AbstractFacebookPrivateGroupAttibute, SoftControlModel):
    product = models.OneToOneField(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.FACEBOOK_PRIVATE_GROUP
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product")
    )

    # Inheritance from .abstracts

    class Meta:
        verbose_name = _("Facebook Private Group")
        verbose_name_plural = _("Facebook Private Groups")
        ordering = ("pk",)

    def __str__(self):
        return self.product.name


@reversion.register()
class SupportSale(AbstractSupportSaleAttibute, SoftControlModel):
    product = models.OneToOneField(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.SUPPORT_SALE
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product")
    )

    # Inheritance from .abstracts

    class Meta:
        verbose_name = _("Support Sale")
        verbose_name_plural = _("Support Sales")
        ordering = ("pk",)

    def __str__(self):
        return self.product.name


@reversion.register()
class Gift(AbstractGiftAttibute, SoftControlModel):
    product = models.OneToOneField(
        Product,
        limit_choices_to={
            'product_type': ProductTypeChoice.GIFT
        },
        on_delete=models.DO_NOTHING,
        verbose_name=_("Product")
    )

    # Inheritance from .abstracts

    class Meta:
        verbose_name = _("Gift")
        verbose_name_plural = _("Gifts")
        ordering = ("pk",)

    def __str__(self):
        return self.product.name
