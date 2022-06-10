from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProductTaxTypeChoice(models.IntegerChoices):
    EXCLUDE_VAT = 1, _("Exclude Vat")
    INCLUDE_VAT_7Persent = 2, ("Include VAT 7%")


class ProductStatusChoice(models.IntegerChoices):
    DRAFT = 1, _("Draft")
    PUBLISHED = 2, _("Published")
    UNPUBLICHED = 3, _("Unpublished")


class ProductImageDisplayTypeChoice(models.IntegerChoices):
    MOBILE = 1, _("Mobile")
    DESKTOP = 2, _("Desktop")
    TABLET = 3, _("Tablet")
