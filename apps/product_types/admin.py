from .forms import CourseBookForm
from .forms import CourseBundleForm
from .forms import CourseEduGadgetForm
from .forms import CourseForm
from .forms import CourseServiceForm
from .forms import EDocumentForm
from .forms import EduGadgetBundleForm
from .forms import EduGadgetForm
from .forms import ExternalCourseForm
from .forms import ExternalExamForm
from .forms import FacebookPrivateGroupForm
from .forms import GiftForm
from .forms import PackagingForm
from .forms import SimulationTestForm
from .forms import SupportSaleForm
from .models import Course
from .models import CourseBook
from .models import CourseBundle
from .models import CourseEduGadget
from .models import CourseService
from .models import EDocument
from .models import EduGadget
from .models import EduGadgetBundle
from .models import ExternalCourse
from .models import ExternalExam
from .models import FacebookPrivateGroup
from .models import Gift
from .models import Packaging
from .models import SimulationTest
from .models import SupportSale
from apps.commons.admin.mixins import ControlAdmin
from django.contrib import admin
from reversion.admin import VersionAdmin


@admin.register(CourseBook)
class CourseBookAdmin(ControlAdmin, VersionAdmin):
    form = CourseBookForm
    raw_id_fields = [
        "product",
    ]
    list_display = [
        "product",
        "isbn",
        "number_of_page",
    ]


@admin.register(CourseBundle)
class CourseBundleAdmin(ControlAdmin, VersionAdmin):
    form = CourseBundleForm
    raw_id_fields = [
        "product",
    ]
    list_display = [
        "product",
        "lifetime_limit",
        "lifetime_limit_unit"
    ]


@admin.register(CourseService)
class CourseServiceAdmin(ControlAdmin, VersionAdmin):
    form = CourseServiceForm
    raw_id_fields = [
        "product",
    ]
    list_display = [
        "product",
        "time_limit",
        "time_limit_unit",
        "pause_limit"
    ]


@admin.register(Course)
class CourseAdmin(ControlAdmin, VersionAdmin):
    form = CourseForm
    raw_id_fields = [
        "product",
    ]
    list_display = [
        "product",
        "lifetime_limit",
        "lifetime_limit_unit"
    ]


@admin.register(EDocument)
class EDocumentAdmin(ControlAdmin, VersionAdmin):
    form = EDocumentForm
    raw_id_fields = [
        "product",
    ]
    list_display = [
        "product",
    ]


@admin.register(EduGadgetBundle)
class EduGadgetBundleAdmin(ControlAdmin, VersionAdmin):
    form = EduGadgetBundleForm
    raw_id_fields = [
        "product",
    ]
    list_display = [
        "product",
    ]


@admin.register(EduGadget)
class EduGadgetAdmin(ControlAdmin, VersionAdmin):
    form = EduGadgetForm
    raw_id_fields = [
        "product",
    ]
    list_display = [
        "product",
        "lifetime_limit",
        "lifetime_limit_unit"
    ]


@admin.register(SimulationTest)
class SimulationTestAdmin(ControlAdmin, VersionAdmin):
    form = SimulationTestForm
    raw_id_fields = [
        "product",
    ]
    list_display = [
        "product",
        "time_limit",
        "time_limit_unit",
        "pause_limit"
    ]


@admin.register(FacebookPrivateGroup)
class FacebookPrivateGroupAdmin(ControlAdmin, VersionAdmin):
    form = FacebookPrivateGroupForm
    raw_id_fields = [
        "product",
    ]
    list_display = [
        "product",
    ]


@admin.register(ExternalCourse)
class ExternalCourseAdmin(ControlAdmin, VersionAdmin):
    form = ExternalCourseForm
    raw_id_fields = [
        "product",
    ]
    list_display = [
        "product",
        "lifetime_limit",
        "lifetime_limit_unit",
    ]


@admin.register(ExternalExam)
class ExternalExamAdmin(ControlAdmin, VersionAdmin):
    form = ExternalExamForm
    raw_id_fields = [
        "product",
    ]
    list_display = [
        "product",
        "time_limit",
        "time_limit_unit",
        "pause_limit",
    ]


@admin.register(SupportSale)
class SupportSaleAdmin(ControlAdmin, VersionAdmin):
    form = SupportSaleForm
    raw_id_fields = [
        "product",
    ]
    list_display = [
        "product",
    ]


@admin.register(CourseEduGadget)
class CourseEduGadgetAdmin(ControlAdmin, VersionAdmin):
    form = CourseEduGadgetForm
    raw_id_fields = [
        "product",
    ]
    list_display = [
        "product",
        "lifetime_limit",
        "lifetime_limit_unit",
    ]


@admin.register(Packaging)
class PackagingAdmin(ControlAdmin, VersionAdmin):
    form = PackagingForm
    raw_id_fields = [
        "product",
    ]
    list_display = [
        "product",
        "width",
        "width_unit",
        "length",
        "length_unit",
        "height",
        "height_unit",
    ]


@admin.register(Gift)
class GiftAdmin(ControlAdmin, VersionAdmin):
    form = GiftForm
    raw_id_fields = [
        "product",
    ]
    list_display = [
        "product",
    ]
