from .forms import ProductGroupForm
from .models import ProductGroup
from apps.commons.admin.mixins import ControlAdmin
from django.contrib import admin
from reversion.admin import VersionAdmin


@admin.register(ProductGroup)
class ProductGroupAdmin(ControlAdmin, VersionAdmin):
    form = ProductGroupForm
    list_display = [
        "name",
        "lms_id",
        "slug"
    ]
