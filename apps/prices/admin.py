from .forms import CourseBookOptionalForm
from .forms import CourseBundleOptionalForm
from .forms import CourseEduGadgetOptionalForm
from .forms import CourseOptionalForm
from .forms import CourseServiceOptionalForm
from .forms import EDocumentOptionalForm
from .forms import EduGadgetBundleOptionalForm
from .forms import EduGadgetOptionalForm
from .forms import ExternalCourseOptionalForm
from .forms import ExternalExamOptionalForm
from .forms import FacebookPrivateGroupOptionalForm
from .forms import GiftOptionalForm
from .forms import PackagingOptionalForm
from .forms import PriceForm
from .forms import PriceProductForm
from .forms import SimulationTestOptionalForm
from .forms import SupportSaleOptionalForm
from .models import CourseBookOptional
from .models import CourseBundleOptional
from .models import CourseEduGadgetOptional
from .models import CourseOptional
from .models import CourseServiceOptional
from .models import EDocumentOptional
from .models import EduGadgetBundleOptional
from .models import EduGadgetOptional
from .models import ExternalCourseOptional
from .models import ExternalExamOptional
from .models import FacebookPrivateGroupOptional
from .models import GiftOptional
from .models import PackagingOptional
from .models import Price
from .models import PriceProduct
from .models import SimulationTestOptional
from .models import SupportSaleOptional
from apps.commons.admin.mixins import ControlAdmin
from django.contrib import admin
from reversion.admin import VersionAdmin


class PriceProductInline(admin.TabularInline):
    model = PriceProduct
    form = PriceProductForm
    raw_id_fields = [
        "product",
    ]
    extra = 1
    show_change_link = True


@admin.register(Price)
class PriceAdmin(ControlAdmin, VersionAdmin):
    form = PriceForm
    inlines = [
        PriceProductInline
    ]
    raw_id_fields = [
        "reference_product",
    ]
    list_display = [
        "code",
        "name",
        "description",
        "price_type",
        "price",
        "reference_product",
        "price_status",
        "price_products"
    ]

    def price_products(self, obj):
        if obj.products.exists():
            return ", ".join(
                obj.products.values_list("name", flat=True)
            )
        return "-"


@admin.register(CourseBookOptional)
class CourseBookOptionalAdmin(ControlAdmin, VersionAdmin):
    form = CourseBookOptionalForm
    raw_id_fields = [
        "price_product",
        "product_chain"
    ]
    list_display = [
        "price_product",
        "product_chain",
        "product_chain_type",
        "isbn",
        "number_of_page",
        "width",
        "width_unit",
        "length",
        "length_unit",
        "height",
        "height_unit",
    ]


@admin.register(CourseBundleOptional)
class CourseBundleOptionalAdmin(ControlAdmin, VersionAdmin):
    form = CourseBundleOptionalForm
    raw_id_fields = [
        "price_product",
        "product_chain"
    ]
    list_display = [
        "price_product",
        "product_chain",
        "product_chain_type",
    ]


@admin.register(CourseServiceOptional)
class CourseServiceOptionalAdmin(ControlAdmin, VersionAdmin):
    form = CourseServiceOptionalForm
    raw_id_fields = [
        "price_product",
        "product_chain"
    ]
    list_display = [
        "price_product",
        "product_chain",
        "product_chain_type",
        "time_limit",
        "time_limit_unit",
        "pause_limit",

    ]


@admin.register(CourseOptional)
class CourseOptionalAdmin(ControlAdmin, VersionAdmin):
    form = CourseOptionalForm
    raw_id_fields = [
        "price_product",
        "product_chain"
    ]
    list_display = [
        "price_product",
        "product_chain",
        "product_chain_type",
        "lifetime_limit",
        "lifetime_limit_unit",
    ]


@admin.register(EDocumentOptional)
class EDocumentOptionalAdmin(ControlAdmin, VersionAdmin):
    form = EDocumentOptionalForm
    raw_id_fields = [
        "price_product",
        "product_chain"
    ]
    list_display = [
        "price_product",
        "product_chain",
        "product_chain_type",
    ]


@admin.register(EduGadgetBundleOptional)
class EduGadgetBundleOptionalAdmin(ControlAdmin, VersionAdmin):
    form = EduGadgetBundleOptionalForm
    raw_id_fields = [
        "price_product",
        "product_chain"
    ]
    list_display = [
        "price_product",
        "product_chain",
        "product_chain_type",
    ]


@admin.register(EduGadgetOptional)
class EduGadgetOptionalAdmin(ControlAdmin, VersionAdmin):
    form = EduGadgetOptionalForm
    raw_id_fields = [
        "price_product",
        "product_chain"
    ]
    list_display = [
        "price_product",
        "product_chain",
        "product_chain_type",
        "lifetime_limit",
        "lifetime_limit_unit",
    ]


@admin.register(SimulationTestOptional)
class SimulationTestOptionalAdmin(ControlAdmin, VersionAdmin):
    form = SimulationTestOptionalForm
    raw_id_fields = [
        "price_product",
        "product_chain"
    ]
    list_display = [
        "price_product",
        "product_chain",
        "product_chain_type",
        "time_limit",
        "time_limit_unit",
        "pause_limit",
    ]


@admin.register(FacebookPrivateGroupOptional)
class FacebookPrivateGroupOptionalAdmin(ControlAdmin, VersionAdmin):
    form = FacebookPrivateGroupOptionalForm
    raw_id_fields = [
        "price_product",
        "product_chain"
    ]
    list_display = [
        "price_product",
        "product_chain",
        "product_chain_type",
    ]


@admin.register(ExternalCourseOptional)
class ExternalCourseOptionalAdmin(ControlAdmin, VersionAdmin):
    form = ExternalCourseOptionalForm
    raw_id_fields = [
        "price_product",
        "product_chain"
    ]
    list_display = [
        "price_product",
        "product_chain",
        "product_chain_type",
        "lifetime_limit",
        "lifetime_limit_unit",
    ]


@admin.register(ExternalExamOptional)
class ExternalExamAdmin(ControlAdmin, VersionAdmin):
    form = ExternalExamOptionalForm
    raw_id_fields = [
        "price_product",
        "product_chain"
    ]
    list_display = [
        "price_product",
        "product_chain",
        "product_chain_type",
        "time_limit",
        "time_limit_unit",
        "pause_limit",
    ]


@admin.register(SupportSaleOptional)
class SupportSaleOptionalAdmin(ControlAdmin, VersionAdmin):
    form = SupportSaleOptionalForm
    raw_id_fields = [
        "price_product",
        "product_chain"
    ]
    list_display = [
        "price_product",
        "product_chain",
        "product_chain_type",
    ]


@admin.register(CourseEduGadgetOptional)
class CourseEduGadgetOptionalAdmin(ControlAdmin, VersionAdmin):
    form = CourseEduGadgetOptionalForm
    raw_id_fields = [
        "price_product",
        "product_chain"
    ]
    list_display = [
        "price_product",
        "product_chain",
        "product_chain_type",
        "lifetime_limit",
        "lifetime_limit_unit",
    ]


@admin.register(PackagingOptional)
class PackagingOptionalAdmin(ControlAdmin, VersionAdmin):
    form = PackagingOptionalForm
    raw_id_fields = [
        "price_product",
        "product_chain"
    ]
    list_display = [
        "price_product",
        "product_chain",
        "product_chain_type",
        "width",
        "width_unit",
        "length",
        "length_unit",
        "height",
        "height_unit",
    ]


@admin.register(GiftOptional)
class GiftOptionalAdmin(ControlAdmin, VersionAdmin):
    form = GiftOptionalForm
    raw_id_fields = [
        "price_product",
        "product_chain"
    ]
    list_display = [
        "price_product",
        "product_chain",
        "product_chain_type",
    ]
