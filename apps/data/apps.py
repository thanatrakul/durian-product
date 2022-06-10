from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.data'
    verbose_name = _("Data")
