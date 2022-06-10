from .serializers import CourseBookSerializer
from .serializers import CourseBundleSerializer
from .serializers import CourseEduGadgetSerializer
from .serializers import CourseSerializer
from .serializers import CourseServiceSerializer
from .serializers import EDocumentSerializer
from .serializers import EduGadgetBundleSerializer
from .serializers import EduGadgetSerializer
from .serializers import ExternalCourseSerailizer
from .serializers import ExternalExamSerializer
from .serializers import FacebookPrivateGroupSerailizer
from .serializers import GiftSerializer
from .serializers import PackagingSerializer
from .serializers import SimulationTestSerializer
from .serializers import SupportSaleSerializer
from apps.commons.api.viewsets import CRUDViewsetMixin
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


class CourseBookViewSet(CRUDViewsetMixin):
    serializer_class = CourseBookSerializer
    queryset = CourseBook.objects.all()


class CourseBundleViewSet(CRUDViewsetMixin):
    serializer_class = CourseBundleSerializer
    queryset = CourseBundle.objects.all()


class CourseServiceViewSet(CRUDViewsetMixin):
    serializer_class = CourseServiceSerializer
    queryset = CourseService.objects.all()


class CourseViewSet(CRUDViewsetMixin):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class EDocumentViewSet(CRUDViewsetMixin):
    serializer_class = EDocumentSerializer
    queryset = EDocument.objects.all()


class EduGadgetBundleViewSet(CRUDViewsetMixin):
    serializer_class = EduGadgetBundleSerializer
    queryset = EduGadgetBundle.objects.all()


class EduGadgetViewSet(CRUDViewsetMixin):
    serializer_class = EduGadgetSerializer
    queryset = EduGadget.objects.all()


class SimulationTestViewSet(CRUDViewsetMixin):
    serializer_class = SimulationTestSerializer
    queryset = SimulationTest.objects.all()


class FacebookPrivateGroupViewSet(CRUDViewsetMixin):
    serializer_class = FacebookPrivateGroupSerailizer
    queryset = FacebookPrivateGroup.objects.all()


class ExternalCourseViewSet(CRUDViewsetMixin):
    serializer_class = ExternalCourseSerailizer
    queryset = ExternalCourse.objects.all()


class ExternalExamViewSet(CRUDViewsetMixin):
    serializer_class = ExternalExamSerializer
    queryset = ExternalExam.objects.all()


class SupportSaleViewSet(CRUDViewsetMixin):
    serializer_class = SupportSaleSerializer
    queryset = SupportSale.objects.all()


class PackagingViewSet(CRUDViewsetMixin):
    serializer_class = PackagingSerializer
    queryset = Packaging.objects.all()


class CourseEduGadgetViewSet(CRUDViewsetMixin):
    serializer_class = CourseEduGadgetSerializer
    queryset = CourseEduGadget.objects.all()


class GiftViewSet(CRUDViewsetMixin):
    serializer_class = GiftSerializer
    queryset = Gift.objects.all()
