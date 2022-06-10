from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ProductGroupsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.product_groups'
    verbose_name = _("Product Groups")
