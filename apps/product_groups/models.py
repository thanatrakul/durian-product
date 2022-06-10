import reversion

from apps.commons.models.mixins import SoftControlModel
from django.db import models
from django.utils.translation import ugettext_lazy as _


@reversion.register()
class ProductGroup(SoftControlModel):
    name = models.CharField(
        max_length=256,
        verbose_name=_("Group name")
    )
    lms_id = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=("LMS ID")
    )
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_("Slug"))

    class Meta:
        verbose_name = _("Product Group")
        verbose_name_plural = _("Product Groups")
        ordering = ("pk",)
        unique_together = [
            ("slug", "live")
        ]

    def __str__(self):
        return self.name
