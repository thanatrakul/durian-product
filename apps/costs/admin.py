from django.contrib import admin
from reversion.admin import VersionAdmin
from apps.commons.admin.mixins import ControlAdmin
from .forms import ProductCostForm
from .models import ProductCost


@admin.register(ProductCost)
class ProductCostAdmin(ControlAdmin, VersionAdmin):
    form = ProductCostForm
    raw_id_fields = [
        "product",
    ]
    show_change_link = True
    list_display = [
        "product",
        "cost",
    ]
