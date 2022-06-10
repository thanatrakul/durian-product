from apps.commons.api.mixins import CRUDSerializerMixin
from apps.prices.models import CourseBookOptional
from apps.prices.models import CourseBundleOptional
from apps.prices.models import CourseEduGadgetOptional
from apps.prices.models import CourseOptional
from apps.prices.models import CourseServiceOptional
from apps.prices.models import EDocumentOptional
from apps.prices.models import EduGadgetBundleOptional
from apps.prices.models import EduGadgetOptional
from apps.prices.models import ExternalCourseOptional
from apps.prices.models import ExternalExamOptional
from apps.prices.models import FacebookPrivateGroupOptional
from apps.prices.models import GiftOptional
from apps.prices.models import PackagingOptional
from apps.prices.models import Price
from apps.prices.models import PriceProduct
from apps.prices.models import SimulationTestOptional
from apps.prices.models import SupportSaleOptional


class PriceSerializer(CRUDSerializerMixin):

    class Meta:
        model = Price
        fields = [
            "id",
            "code",
            "name",
            "description",
            "price_type",
            "price",
            "reference_product",
            "products",
            "live"
        ]

    def get_price_products(self, obj):
        dataset = obj.products.through.objects.all()
        return PriceSerializer(dataset, many=True).data


class PriceProductSerializer(CRUDSerializerMixin):

    class Meta:
        model = PriceProduct
        fields = [
            "id",
            "price",
            "product",
            "quantity",
            "product_group",
            "live",

        ]


class CourseBookOptionalSerializer(CRUDSerializerMixin):

    class Meta:
        model = CourseBookOptional
        fields = [
            "id",
            "price_product",
            "product_chain",
            "product_chain_type",
            "isbn",
        ]


class CourseBundleOptionalSerializer(CRUDSerializerMixin):

    class Meta:
        model = CourseBundleOptional
        fields = [
            "id",
            "price_product",
        ]


class CourseOptionalSerializer(CRUDSerializerMixin):

    class Meta:
        model = CourseOptional
        fields = [
            "id",
            "price_product",
        ]


class CourseServiceOptionalSerializer(CRUDSerializerMixin):

    class Meta:
        model = CourseServiceOptional
        fields = [
            "id",
            "price_product",
            "product_chain",
            "product_chain_type",
        ]


class EDocumentOptionalSerializer(CRUDSerializerMixin):

    class Meta:
        model = EDocumentOptional
        fields = [
            "id",
            "price_product",
            "product_chain",
            "product_chain_type",
        ]


class EduGadgetBundleOptionalSerializer(CRUDSerializerMixin):

    class Meta:
        model = EduGadgetBundleOptional
        fields = [
            "id",
            "price_product",
        ]


class EduGadgetOptionalSerializer(CRUDSerializerMixin):

    class Meta:
        model = EduGadgetOptional
        fields = [
            "id",
            "price_product",
            "product_chain",
            "product_chain_type",
        ]


class SimulationTestOptionalSerializer(CRUDSerializerMixin):

    class Meta:
        model = SimulationTestOptional
        fields = [
            "id",
            "price_product",
            "product_chain",
            "product_chain_type",
        ]


class FacebookPrivateGroupOptionalSerailizer(CRUDSerializerMixin):
    class Meta:
        model = FacebookPrivateGroupOptional
        fields = [
            "id",
            "price_product",
            "product_chain",
            "product_chain_type",
        ]


class ExternalCourseOptionalSerailizer(CRUDSerializerMixin):
    class Meta:
        model = ExternalCourseOptional
        fields = [
            "id",
            "price_product",
            "product_chain",
            "product_chain_type",
        ]


class ExternalExamOptionalSerializer(CRUDSerializerMixin):
    class Meta:
        model = ExternalExamOptional
        fields = [
            "id",
            "price_product",
            "product_chain",
            "product_chain_type",
        ]


class SupportSaleOptionalSerializer(CRUDSerializerMixin):
    class Meta:
        model = SupportSaleOptional
        fields = [
            "id",
            "price_product",
            "product_chain",
            "product_chain_type",
        ]


class CourseEduGadgetOptionalSerializer(CRUDSerializerMixin):
    class Meta:
        model = CourseEduGadgetOptional
        fields = [
            "id",
            "price_product",
            "product_chain",
            "product_chain_type",
        ]


class PackagingOptionalSerializer(CRUDSerializerMixin):
    class Meta:
        model = PackagingOptional
        fields = [
            "id",
            "price_product",
            "product_chain",
            "product_chain_type",
        ]


class GiftOptionalSerializer(CRUDSerializerMixin):
    class Meta:
        model = GiftOptional
        fields = [
            "id",
            "price_product",
            "product_chain",
            "product_chain_type",
        ]
