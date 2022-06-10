from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProductTypeChoice(models.IntegerChoices):
    COURSE = 1, _("Course")
    COURSE_BUNDLE = 2, _("Course Bundle")
    COURSE_BOOK = 3, _("Course Book")
    COURSE_SERVICE = 4, _("Course Service")
    EDUGADGET = 5, _("EduGadget")
    EDUGADGET_BUNDLE = 6, _("EduGadget Bundle")
    SIMULATION_TEST = 7, _("Simulation Test")
    E_DOCUMENT = 8, _("E-Document")
    COURSE_EduGadget = 9, _("Course EduGadget")
    PACKAGING = 10, _("Packaging")
    EXTERNAL_CAURSE = 11, _("External course")
    EXTERNAL_EXAM = 12, _("External Exam")
    FACEBOOK_PRIVATE_GROUP = 13, _("Facebook Private Group")
    SUPPORT_SALE = 14, _("Support Sale")
    GIFT = 15, _("Gift")


class LengthSIUnitChoice(models.IntegerChoices):
    MM = 1, _("Millimeter")
    CM = 2, _("Centimeter")


class TimeSIUnitChoice(models.IntegerChoices):
    SECOND = 1, _("Second")
    MINUTE = 2, _("Minute(s)")
    HOUR = 3, _("Hour")
    DAY = 4, _("Day")
