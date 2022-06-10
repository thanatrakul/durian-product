from apps.commons.api.mixins import CRUDSerializerMixin
from apps.product_types.models import Course
from apps.product_types.models import CourseBook
from apps.product_types.models import CourseBundle
from apps.product_types.models import CourseEduGadget
from apps.product_types.models import CourseService
from apps.product_types.models import EDocument
from apps.product_types.models import EduGadget
from apps.product_types.models import EduGadgetBundle
from apps.product_types.models import ExternalCourse
from apps.product_types.models import ExternalExam
from apps.product_types.models import FacebookPrivateGroup
from apps.product_types.models import Gift
from apps.product_types.models import Packaging
from apps.product_types.models import SimulationTest
from apps.product_types.models import SupportSale


class CourseBookSerializer(CRUDSerializerMixin):
    class Meta:
        model = CourseBook
        fields = [
            "id",
            "product",
            "isbn",
            "number_of_page",
            "width",
            "width_unit",
            "length",
            "length_unit",
            "height",
            "height_unit",
            "live",
        ]


class CourseBundleSerializer(CRUDSerializerMixin):
    class Meta:
        model = CourseBundle
        fields = [
            "id",
            "product",
            "live",
        ]


class CourseServiceSerializer(CRUDSerializerMixin):
    class Meta:
        model = CourseService
        fields = [
            "id",
            "product",
            "time_limit",
            "time_limit_unit",
            "pause_limit",
            "live",

        ]


class CourseSerializer(CRUDSerializerMixin):
    class Meta:
        model = Course
        fields = [
            "id",
            "product",
            "lifetime_limit",
            "lifetime_limit_unit",
            "live",

        ]


class EDocumentSerializer(CRUDSerializerMixin):
    class Meta:
        model = EDocument
        fields = [
            "id",
            "product",
            "live",

        ]


class EduGadgetBundleSerializer(CRUDSerializerMixin):
    class Meta:
        model = EduGadgetBundle
        fields = [
            "id",
            "product",
            "live",
        ]


class EduGadgetSerializer(CRUDSerializerMixin):
    class Meta:
        model = EduGadget
        fields = [
            "id",
            "product",
            "lifetime_limit",
            "lifetime_limit_unit",
            "product",
            "live",
        ]


class SimulationTestSerializer(CRUDSerializerMixin):
    class Meta:
        model = SimulationTest
        fields = [
            "id",
            "product",
            "time_limit",
            "time_limit_unit",
            "pause_limit",
            "live",
        ]


class FacebookPrivateGroupSerailizer(CRUDSerializerMixin):
    class Meta:
        model = FacebookPrivateGroup
        fields = [
            "id",
            "product",
            "live",

        ]


class ExternalCourseSerailizer(CRUDSerializerMixin):
    class Meta:
        model = ExternalCourse
        fields = [
            "id",
            "product",
            "lifetime_limit",
            "lifetime_limit_unit",
            "live",

        ]


class ExternalExamSerializer(CRUDSerializerMixin):
    class Meta:
        model = ExternalExam
        fields = [
            "id",
            "product",
            "time_limit",
            "time_limit_unit",
            "pause_limit",
            "live",
        ]


class SupportSaleSerializer(CRUDSerializerMixin):
    class Meta:
        model = SupportSale
        fields = [
            "id",
            "product",
            "live",
        ]


class CourseEduGadgetSerializer(CRUDSerializerMixin):
    class Meta:
        model = CourseEduGadget
        fields = [
            "id",
            "product",
            "lifetime_limit",
            "lifetime_limit_unit",
            "live",
        ]


class PackagingSerializer(CRUDSerializerMixin):
    class Meta:
        model = Packaging
        fields = [
            "id",
            "product",
            "width",
            "width_unit",
            "length",
            "length_unit",
            "height",
            "height_unit",
            "live",

        ]


class GiftSerializer(CRUDSerializerMixin):
    class Meta:
        model = Gift
        fields = [
            "id",
            "product",
            "live",
        ]
