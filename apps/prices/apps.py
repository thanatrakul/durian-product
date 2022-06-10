from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PricesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.prices'
    verbose_name = _("Prices")
