from .serializers import CourseBookOptionalSerializer
from .serializers import CourseBundleOptionalSerializer
from .serializers import CourseEduGadgetOptionalSerializer
from .serializers import CourseOptionalSerializer
from .serializers import CourseServiceOptionalSerializer
from .serializers import EDocumentOptionalSerializer
from .serializers import EduGadgetBundleOptionalSerializer
from .serializers import EduGadgetOptionalSerializer
from .serializers import ExternalCourseOptionalSerailizer
from .serializers import ExternalExamOptionalSerializer
from .serializers import FacebookPrivateGroupOptionalSerailizer
from .serializers import GiftOptionalSerializer
from .serializers import PackagingOptionalSerializer
from .serializers import PriceProductSerializer
from .serializers import PriceSerializer
from .serializers import SimulationTestOptionalSerializer
from .serializers import SupportSaleOptionalSerializer
from apps.commons.api.viewsets import CRUDViewsetMixin
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


class PriceViewSet(CRUDViewsetMixin):
    serializer_class = PriceSerializer
    queryset = Price.objects.all()


class PriceProductViewSet(CRUDViewsetMixin):
    serializer_class = PriceProductSerializer
    queryset = PriceProduct.objects.all()


class CourseBookOptionalViewSet(CRUDViewsetMixin):
    serializer_class = CourseBookOptionalSerializer
    queryset = CourseBookOptional.objects.all()


class CourseBundleOptionalViewSet(CRUDViewsetMixin):
    serializer_class = CourseBundleOptionalSerializer
    queryset = CourseBundleOptional.objects.all()


class CourseOptionalViewSet(CRUDViewsetMixin):
    serializer_class = CourseOptionalSerializer
    queryset = CourseOptional.objects.all()


class CourseServiceOptionalViewSet(CRUDViewsetMixin):
    serializer_class = CourseServiceOptionalSerializer
    queryset = CourseServiceOptional.objects.all()


class EDocumentOptionalViewSet(CRUDViewsetMixin):
    serializer_class = EDocumentOptionalSerializer
    queryset = EDocumentOptional.objects.all()


class EduGadgetBundleOptionalViewSet(CRUDViewsetMixin):
    serializer_class = EduGadgetBundleOptionalSerializer
    queryset = EduGadgetBundleOptional.objects.all()


class EduGadgetOptionalViewSet(CRUDViewsetMixin):
    serializer_class = EduGadgetOptionalSerializer
    queryset = EduGadgetOptional.objects.all()


class SimulationTestOptionalViewSet(CRUDViewsetMixin):
    serializer_class = SimulationTestOptionalSerializer
    queryset = SimulationTestOptional.objects.all()


class ExternalCourseOptionalViewSet(CRUDViewsetMixin):
    serializer_class = ExternalCourseOptionalSerailizer
    queryset = ExternalCourseOptional.objects.all()


class ExternalExamOptionalViewSet(CRUDViewsetMixin):
    serializer_class = ExternalExamOptionalSerializer
    queryset = ExternalExamOptional.objects.all()


class FacebookPrivateGroupOptionalViewSet(CRUDViewsetMixin):
    serializer_class = FacebookPrivateGroupOptionalSerailizer
    queryset = FacebookPrivateGroupOptional.objects.all()


class SupportSaleOptionalViewSet(CRUDViewsetMixin):
    serializer_class = SupportSaleOptionalSerializer
    queryset = SupportSaleOptional.objects.all()


class PackagingOptionalViewSet(CRUDViewsetMixin):
    serializer_class = PackagingOptionalSerializer
    queryset = PackagingOptional.objects.all()


class CourseEduGadgetOptionalViewSet(CRUDViewsetMixin):
    serializer_class = CourseEduGadgetOptionalSerializer
    queryset = CourseEduGadgetOptional.objects.all()


class GiftOptionalViewSet(CRUDViewsetMixin):
    serializer_class = GiftOptionalSerializer
    queryset = GiftOptional.objects.all()
