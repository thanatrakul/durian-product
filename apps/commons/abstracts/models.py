from django.db import models
from django.db.models import F
from django.db.models import Max
from django.utils.translation import ugettext_lazy as _
from uuid import uuid4


class AbstractToken(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class AbstractUTM(models.Model):
    """
        UTM (https://ga-dev-tools.appspot.com/campaign-url-builder/)
    """

    utm_source = models.CharField(
        max_length=255,
        default="opendurian",
        help_text=_("Use utm_source to identify a search engine, newsletter name, or other source. Example: google, newsletter"),
        verbose_name=_("UTM Source")
    )
    utm_medium = models.CharField(
        max_length=255,
        help_text=_("Use utm_medium to identify a medium such as email or cost-per- click. Example: cpc, banner, email"),
        verbose_name=_("UTM Medium")
    )
    utm_campaign = models.CharField(
        max_length=255,
        help_text=_("Used for keyword analysis. Use utm_campaign to identify a specific product promotion or strategic campaign. Example: utm_campaign=spring_sale"),
        verbose_name=_("UTM Campaign")
    )
    utm_term = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Used for paid search. Use utm_term to note the keywords for this ad."),
        verbose_name=_("UTM Term")
    )
    utm_content = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Used for A/B testing and content-targeted ads. Use utm_content to differentiate ads or links that point to the same URL. Examples: logolink or textlink"),
        verbose_name=_("UTM Content")
    )

    class Meta:
        abstract = True



class AbstractOrderingField(models.Model):
    ordering = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        verbose_name=_('Ordering')
    )

    __original_ordering = None
    # __original_queryset = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_ordering = self.ordering
        # self.__original_queryset = self.get_ordering_field_queryset()

    def get_ordering_field_queryset(self):
        raise NotImplementedError(_("Unknown ordering queryset"))

    def get_max_ordering(self):
        qs = self.get_ordering_field_queryset()
        existing_max = qs.aggregate(Max("ordering"))
        existing_max = existing_max.get("ordering__max")
        return existing_max

    def update_exists_queryset(self):
        qs = self.get_ordering_field_queryset()
        if self.__original_ordering is not None:
            reduce_qs = qs.filter(ordering__gt=self.__original_ordering)
            reduce_qs.update(ordering=F("ordering") - 1)
        if self.ordering is not None:
            increase_qs = qs.filter(ordering__gte=self.ordering)
            increase_qs.update(ordering=F("ordering") + 1)

    def update_new_queryset(self):
        if self.ordering is not None:
            increase_new_qs = self.get_ordering_field_queryset().filter(ordering__gte=self.ordering)
            increase_new_qs.update(ordering=F("ordering") + 1)

    def save(self, *args, **kwargs):
        if self.pk is None:
            if self.ordering:
                self.update_exists_queryset()
            else:
                existing_max = self.get_max_ordering()
                self.ordering = 0 if existing_max is None else existing_max + 1
        else:
            """
            ORDERING CHANGED
            """
            try:
                self.get_ordering_field_queryset().get(id=self.id)
                if self.__original_ordering != self.ordering:
                    self.update_exists_queryset()
            except Exception as e:
                self.update_new_queryset()
                # self.__original_ordering = self.ordering
            # if self.__original_ordering != self.ordering:
        """
        FOR MIGRATE DATA
        """
        # if self.ordering:
        #     self.update_exists_queryset()
        # else:
        #     existing_max = self.get_max_ordering()
        #     self.ordering = 0 if existing_max is None else existing_max + 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.ordering is not None:
            qs = self.get_ordering_field_queryset()
            qs.filter(ordering__gt=self.ordering).update(
                ordering=F("ordering") - 1
            )
        super().delete(*args, **kwargs)

    class Meta:
        abstract = True



class AbstractTimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        abstract = True
