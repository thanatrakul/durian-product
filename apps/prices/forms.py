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
from apps.commons.forms.mixins import SoftControlControlModelFormMixin


class PriceForm(SoftControlControlModelFormMixin):

    class Meta:
        model = Price
        fields = [
            "code",
            "name",
            "description",
            "price_type",
            "price",
            "reference_product",
            "products",
            "price_status",
            "live"
        ]


class PriceProductForm(SoftControlControlModelFormMixin):

    class Meta:
        model = PriceProduct
        fields = [
            "price",
            "product",
            "quantity",
            "product_group",
            "live"
        ]


class CourseBookOptionalForm(SoftControlControlModelFormMixin):

    class Meta:
        model = CourseBookOptional
        fields = [
            "price_product",

            # Product Chain
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
            "live"
        ]


class CourseBundleOptionalForm(SoftControlControlModelFormMixin):

    class Meta:
        model = CourseBundleOptional
        fields = [
            "price_product",
            "product_chain",
            "product_chain_type",
            "live"
        ]


class CourseServiceOptionalForm(SoftControlControlModelFormMixin):

    class Meta:
        model = CourseServiceOptional
        fields = [
            "price_product",
            "product_chain",
            "product_chain_type",
            "time_limit",
            "time_limit_unit",
            "pause_limit",
            "live"
        ]


class CourseOptionalForm(SoftControlControlModelFormMixin):

    class Meta:
        model = CourseOptional
        fields = [
            "price_product",
            "product_chain",
            "product_chain_type",

            "lifetime_limit",
            "lifetime_limit_unit",
            "live"
        ]


class EDocumentOptionalForm(SoftControlControlModelFormMixin):

    class Meta:
        model = EDocumentOptional
        fields = [
            "price_product",
            "product_chain",
            "product_chain_type",
            "live"
        ]


class EduGadgetBundleOptionalForm(SoftControlControlModelFormMixin):

    class Meta:
        model = EduGadgetBundleOptional
        fields = [
            "price_product",
            "product_chain",
            "product_chain_type",
            "live"
        ]


class EduGadgetOptionalForm(SoftControlControlModelFormMixin):

    class Meta:
        model = EduGadgetOptional
        fields = [
            "price_product",
            "product_chain",
            "product_chain_type",
            "lifetime_limit",
            "lifetime_limit_unit",
            "live"
        ]


class SimulationTestOptionalForm(SoftControlControlModelFormMixin):

    class Meta:
        model = SimulationTestOptional
        fields = [
            "price_product",
            "product_chain",
            "product_chain_type",
            "time_limit",
            "time_limit_unit",
            "pause_limit",
            "live"
        ]


class FacebookPrivateGroupOptionalForm(SoftControlControlModelFormMixin):

    class Meta:
        model = FacebookPrivateGroupOptional
        fields = [
            "price_product",
            "product_chain",
            "product_chain_type",
            "live"
        ]


class ExternalCourseOptionalForm(SoftControlControlModelFormMixin):

    class Meta:
        model = ExternalCourseOptional
        fields = [
            "price_product",
            "product_chain",
            "product_chain_type",
            "lifetime_limit",
            "lifetime_limit_unit",
            "live"
        ]


class ExternalExamOptionalForm(SoftControlControlModelFormMixin):

    class Meta:
        model = ExternalExamOptional
        fields = [
            "price_product",
            "product_chain",
            "product_chain_type",
            "time_limit",
            "time_limit_unit",
            "pause_limit",
            "live"
        ]


class SupportSaleOptionalForm(SoftControlControlModelFormMixin):

    class Meta:
        model = SupportSaleOptional
        fields = [
            "price_product",
            "product_chain",
            "product_chain_type",
            "live"
        ]


class CourseEduGadgetOptionalForm(SoftControlControlModelFormMixin):

    class Meta:
        model = CourseEduGadgetOptional
        fields = [
            "price_product",
            "product_chain",
            "product_chain_type",
            "lifetime_limit",
            "lifetime_limit_unit",
            "live"
        ]


class PackagingOptionalForm(SoftControlControlModelFormMixin):

    class Meta:
        model = PackagingOptional
        fields = [
            "price_product",
            "product_chain",
            "product_chain_type",
            "width",
            "width_unit",
            "length",
            "length_unit",
            "height",
            "height_unit",
            "live"
        ]


class GiftOptionalForm(SoftControlControlModelFormMixin):

    class Meta:
        model = GiftOptional
        fields = [
            "price_product",
            "product_chain",
            "product_chain_type",
            "live"
        ]
