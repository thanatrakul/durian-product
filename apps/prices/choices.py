from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProductChainTypeChoice(models.IntegerChoices):
    DO_NOTHING = 1, _("Do nothing")
    IMMEDIATELY = 2, _("Immediately")
    AFTER_PRIMARY_PRODUCT_DO_NOT_EXIST = 3, _("After primary product do not exist")


class PriceTypeChoice(models.IntegerChoices):
    FULL_PAYMENT = 1, _("Full Payment")
    DEPOSIT = 2, _("Deposit")


class PriceStatusChoice(models.IntegerChoices):
    DARFT = 1, _("Draft")
    PUBLISHED = 2, _("Published")
    SUPPRESSED = 3, _("Suppressed")
    HIDDENED = 4, _("Hideden")
