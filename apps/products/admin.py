from django.contrib import admin
from reversion.admin import VersionAdmin
from apps.commons.admin.mixins import ControlAdmin
from .forms import BundleSetForm
from .forms import BundleSetItemForm
from .forms import ProductForm
from .forms import ProductImageForm
from .models import BundleSet
from .models import BundleSetItem
from .models import Product
from .models import ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    form = ProductImageForm
    raw_id_fields = [
        "product",
    ]
    extra = 1
    show_change_link = True
    list_display = [
        "image",
        "description",
        "alt_image",
        "display_type",
    ]


@admin.register(Product)
class ProductAdmin(ControlAdmin, VersionAdmin):
    form = ProductForm
    inlines = [
        ProductImageInline,
    ]
    list_display = [
        "slug",
        "name",
        "sku_code",
        "lagacy_sku",
        "tax",
        "status",
        "product_type",
    ]


class BundleSetItemInline(admin.TabularInline):
    model = BundleSetItem
    form = BundleSetItemForm
    raw_id_fields = [
        "product",
    ]
    extra = 1
    show_change_link = True
    list_display = [
        "bundle_set",
        "quantity",
    ]


@admin.register(BundleSet)
class BundleSetAdmin(ControlAdmin, VersionAdmin):
    form = BundleSetForm
    inlines = [
        BundleSetItemInline,
    ]
    raw_id_fields = [
        "product",
    ]
    list_display = [
        "name",
        "product",

        # "items"
    ]
