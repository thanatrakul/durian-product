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
from apps.commons.forms.mixins import SoftControlControlModelFormMixin


class CourseBookForm(SoftControlControlModelFormMixin):
    class Meta:
        model = CourseBook
        fields = [
            "product",
            "live",

            # Attributes
            "isbn",
            "number_of_page",
            "width",
            "width_unit",
            "length",
            "length_unit",
            "height",
            "height_unit",
        ]


class CourseBundleForm(SoftControlControlModelFormMixin):
    class Meta:
        model = CourseBundle
        fields = [
            "product",
            "live",

            # Attributes
            "lifetime_limit",
            "lifetime_limit_unit",
        ]


class CourseServiceForm(SoftControlControlModelFormMixin):
    class Meta:
        model = CourseService
        fields = [
            "product",
            "live",

            # Attributes
            "time_limit",
            "time_limit_unit",
            "pause_limit",
        ]


class CourseForm(SoftControlControlModelFormMixin):
    class Meta:
        model = Course
        fields = [
            "product",
            "live",

            # Attributes
            "lifetime_limit",
            "lifetime_limit_unit",
        ]


class EDocumentForm(SoftControlControlModelFormMixin):
    class Meta:
        model = EDocument
        fields = [
            "product",
            "live",

            # Attributes
        ]


class EduGadgetBundleForm(SoftControlControlModelFormMixin):
    class Meta:
        model = EduGadgetBundle
        fields = [
            "product",
            "live",

            # Attributes
        ]


class EduGadgetForm(SoftControlControlModelFormMixin):
    class Meta:
        model = EduGadget
        fields = [
            "product",
            "live",

            # Attributes
            "lifetime_limit",
            "lifetime_limit_unit",
        ]


class SimulationTestForm(SoftControlControlModelFormMixin):
    class Meta:
        model = SimulationTest
        fields = [
            "product",
            "live",

            # Attributes
            "time_limit",
            "time_limit_unit",
            "pause_limit",
        ]


class FacebookPrivateGroupForm(SoftControlControlModelFormMixin):
    class Meta:
        model = FacebookPrivateGroup
        fields = [
            "product",
            "live",

            # Attributes
        ]


class ExternalCourseForm(SoftControlControlModelFormMixin):
    class Meta:
        model = ExternalCourse
        fields = [
            "product",
            "live",

            # Attributes
            "lifetime_limit",
            "lifetime_limit_unit",
        ]


class ExternalExamForm(SoftControlControlModelFormMixin):
    class Meta:
        model = ExternalExam
        fields = [
            "product",
            "live",

            # Attributes
            "time_limit",
            "time_limit_unit",
            "pause_limit",
        ]


class SupportSaleForm(SoftControlControlModelFormMixin):
    class Meta:
        model = SupportSale
        fields = [
            "product",
            "live",

            # Attributes
        ]


class CourseEduGadgetForm(SoftControlControlModelFormMixin):
    class Meta:
        model = CourseEduGadget
        fields = [
            "product",
            "live",

            # Attributes
            "lifetime_limit",
            "lifetime_limit_unit",
        ]


class PackagingForm(SoftControlControlModelFormMixin):
    class Meta:
        model = Packaging
        fields = [
            "product",
            "live",

            # Attributes
            "width",
            "width_unit",
            "length",
            "length_unit",
            "height",
            "height_unit",
        ]


class GiftForm(SoftControlControlModelFormMixin):
    class Meta:
        model = Gift
        fields = [
            "product",
            "live",

            # Attributes
        ]
