from .choices import LengthSIUnitChoice
from .choices import TimeSIUnitChoice
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractCourseBookAttibute(models.Model):

    # Book Info
    isbn = models.CharField(max_length=255, unique=True, verbose_name=_("ISBN"))
    number_of_page = models.PositiveSmallIntegerField(default=0, verbose_name=_("Number of Page"))

    # Width
    width = models.DecimalField(
        default=Decimal(0),
        decimal_places=2,
        max_digits=5,
        verbose_name=_("Width"),
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    width_unit = models.PositiveSmallIntegerField(
        choices=LengthSIUnitChoice.choices,
        default=LengthSIUnitChoice.CM,
        verbose_name=("Width Unit")
    )

    # Length
    length = models.DecimalField(
        default=Decimal(0),
        decimal_places=2,
        max_digits=5,
        verbose_name=_("Length"),
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    length_unit = models.PositiveSmallIntegerField(
        choices=LengthSIUnitChoice.choices,
        default=LengthSIUnitChoice.CM,
        verbose_name=("Length Unit")
    )

    # Height
    height = models.DecimalField(
        default=Decimal(0),
        decimal_places=2,
        max_digits=5,
        verbose_name=_("Height"),
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    height_unit = models.PositiveSmallIntegerField(
        choices=LengthSIUnitChoice.choices,
        default=LengthSIUnitChoice.CM,
        verbose_name=("Height Unit")
    )

    class Meta:
        abstract = True


class AbstractCourseBundleAttibute(models.Model):
    lifetime_limit = models.PositiveSmallIntegerField(default=0, verbose_name=_("Lifetime Limit"))  # day
    lifetime_limit_unit = models.PositiveSmallIntegerField(
        choices=TimeSIUnitChoice.choices,
        default=TimeSIUnitChoice.DAY,
        verbose_name=("Lifetime Limit Unit")
    )

    class Meta:
        abstract = True


class AbstractCourseServiceAttibute(models.Model):

    # Time Limit
    time_limit = models.DecimalField(
        default=Decimal(0),
        decimal_places=2,
        max_digits=5,
        verbose_name=_("Time Limit"),
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    time_limit_unit = models.PositiveSmallIntegerField(
        choices=TimeSIUnitChoice.choices,
        default=TimeSIUnitChoice.MINUTE,
        verbose_name=("time Limit Unit")
    )

    # Pause Limit
    pause_limit = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Time Limit")
    )
    # Pause Limit have only one unit("Times")

    class Meta:
        abstract = True


class AbstractCourseAttibute(models.Model):

    # Lifetime Limit
    lifetime_limit = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_("Lifetime Limit")
    )
    lifetime_limit_unit = models.PositiveSmallIntegerField(
        choices=TimeSIUnitChoice.choices,
        default=TimeSIUnitChoice.DAY,
        verbose_name=("Lifetime Limit Unit")
    )

    class Meta:
        abstract = True


class AbstractEDocumentAttibute(models.Model):
    pass

    class Meta:
        abstract = True


class AbstractEduGadgetBundleAttibute(models.Model):
    pass

    class Meta:
        abstract = True


class AbstractEduGadgetAttibute(models.Model):

    # Lifetime Limit
    lifetime_limit = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_("Lifetime Limit")
    )
    lifetime_limit_unit = models.PositiveSmallIntegerField(
        choices=TimeSIUnitChoice.choices,
        default=TimeSIUnitChoice.DAY,
        verbose_name=("Lifetime Limit Unit")
    )

    class Meta:
        abstract = True


class AbstractSimulationTestAttibute(models.Model):

    # Time Limit
    time_limit = models.DecimalField(
        default=Decimal(0),
        decimal_places=2,
        max_digits=5,
        verbose_name=_("Time Limit")
    )
    time_limit_unit = models.PositiveSmallIntegerField(
        choices=TimeSIUnitChoice.choices,
        default=TimeSIUnitChoice.MINUTE,
        verbose_name=("Time Limit Unit")
    )

    # Pause Limit
    pause_limit = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_("Pause Limit")
    )
    # Pause Limit have only one unit("Times")

    class Meta:
        abstract = True


class AbstractFacebookPrivateGroupAttibute(models.Model):
    pass

    class Meta:
        abstract = True


class AbstractExternalCourseAttibute(models.Model):

    # Lifetime Limit
    lifetime_limit = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_("Lifetime Limit")
    )
    lifetime_limit_unit = models.PositiveSmallIntegerField(
        choices=TimeSIUnitChoice.choices,
        default=TimeSIUnitChoice.DAY,
        verbose_name=("Lifetime Limit Unit")
    )

    class Meta:
        abstract = True


class AbstractExternalExamAttibute(models.Model):

    # Time Limit
    time_limit = models.DecimalField(
        default=Decimal(0),
        decimal_places=2,
        max_digits=5,
        verbose_name=_("Time Limit"),
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    time_limit_unit = models.PositiveSmallIntegerField(
        choices=TimeSIUnitChoice.choices,
        default=TimeSIUnitChoice.MINUTE,
        verbose_name=("Time Limit Unit")
    )

    # Pause Limit
    pause_limit = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_("Pause Limit")
    )
    # Pause Limit have only one unit("Times")

    class Meta:
        abstract = True


class AbstractSupportSaleAttibute(models.Model):
    pass

    class Meta:
        abstract = True


class AbstractCourseEduGadgetAttibute(models.Model):

    # Lifetime Limit
    lifetime_limit = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_("Lifetime Limit")
    )
    lifetime_limit_unit = models.PositiveSmallIntegerField(
        choices=TimeSIUnitChoice.choices,
        default=TimeSIUnitChoice.DAY,
        verbose_name=("Lifetime Limit Unit")
    )

    class Meta:
        abstract = True


class AbstracPackagingAttibute(models.Model):

    # Width
    width = models.DecimalField(
        default=Decimal(0),
        decimal_places=2,
        max_digits=5,
        verbose_name=_("Width"),
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    width_unit = models.PositiveSmallIntegerField(
        choices=LengthSIUnitChoice.choices,
        default=LengthSIUnitChoice.CM,
        verbose_name=("Width Unit")
    )

    # Length
    length = models.DecimalField(
        default=Decimal(0),
        decimal_places=2,
        max_digits=5,
        verbose_name=_("Length"),
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    length_unit = models.PositiveSmallIntegerField(
        choices=LengthSIUnitChoice.choices,
        default=LengthSIUnitChoice.CM,
        verbose_name=("Length Unit")
    )

    # Height
    height = models.DecimalField(
        default=Decimal(0),
        decimal_places=2,
        max_digits=5,
        verbose_name=_("Heigth"),
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    height_unit = models.PositiveSmallIntegerField(
        choices=LengthSIUnitChoice.choices,
        default=LengthSIUnitChoice.CM,
        verbose_name=("Height Unit")
    )

    # Weight

    class Meta:
        abstract = True


class AbstractGiftAttibute(models.Model):
    pass

    class Meta:
        abstract = True
