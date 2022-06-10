from apps.costs.api.viewsets import ProductCostViewSet
from apps.prices.api.viewsets import CourseBookOptionalViewSet
from apps.prices.api.viewsets import CourseBundleOptionalViewSet
from apps.prices.api.viewsets import CourseEduGadgetOptionalViewSet
from apps.prices.api.viewsets import CourseOptionalViewSet
from apps.prices.api.viewsets import CourseServiceOptionalViewSet
from apps.prices.api.viewsets import EDocumentOptionalViewSet
from apps.prices.api.viewsets import EduGadgetBundleOptionalViewSet
from apps.prices.api.viewsets import ExternalCourseOptionalViewSet
from apps.prices.api.viewsets import ExternalExamOptionalViewSet
from apps.prices.api.viewsets import FacebookPrivateGroupOptionalViewSet
from apps.prices.api.viewsets import GiftOptionalViewSet
from apps.prices.api.viewsets import PackagingOptionalViewSet
from apps.prices.api.viewsets import PriceProductViewSet
from apps.prices.api.viewsets import PriceViewSet
from apps.prices.api.viewsets import SimulationTestOptionalViewSet
from apps.prices.api.viewsets import SupportSaleOptionalViewSet
from apps.product_groups.api.viewsets import ProductGroupViewSet
from apps.product_types.api.viewsets import CourseBookViewSet
from apps.product_types.api.viewsets import CourseBundleViewSet
from apps.product_types.api.viewsets import CourseEduGadgetViewSet
from apps.product_types.api.viewsets import CourseServiceViewSet
from apps.product_types.api.viewsets import CourseViewSet
from apps.product_types.api.viewsets import EDocumentViewSet
from apps.product_types.api.viewsets import EduGadgetBundleViewSet
from apps.product_types.api.viewsets import EduGadgetViewSet
from apps.product_types.api.viewsets import ExternalCourseViewSet
from apps.product_types.api.viewsets import ExternalExamViewSet
from apps.product_types.api.viewsets import FacebookPrivateGroupViewSet
from apps.product_types.api.viewsets import GiftViewSet
from apps.product_types.api.viewsets import PackagingViewSet
from apps.product_types.api.viewsets import SimulationTestViewSet
from apps.product_types.api.viewsets import SupportSaleViewSet
from apps.products.api.viewsets import BundleSetItemViewSet
from apps.products.api.viewsets import BundleSetViewSet
from apps.products.api.viewsets import ProductImageItemViewSet
from apps.products.api.viewsets import ProductViewSet
from apps.users.api.views import UserViewSet
from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter


# Switch
if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


# APIs

# Users
router.register("users", UserViewSet)


# Costs
router.register("costs/product_costs", ProductCostViewSet)


# Prices
router.register("prices/prices", PriceViewSet)
router.register("prices/price_products", PriceProductViewSet)
router.register("prices/optional/course_books", CourseBookOptionalViewSet)
router.register("prices/optional/course_bundles", CourseBundleOptionalViewSet)
router.register("prices/optional/course_services", CourseServiceOptionalViewSet)
router.register("prices/optional/courses", CourseOptionalViewSet)
router.register("prices/optional/e_documents", EDocumentOptionalViewSet)
router.register("prices/optional/edugadget_bundles", EduGadgetBundleOptionalViewSet)
router.register("prices/optional/edugadgets", EduGadgetBundleOptionalViewSet)
router.register("prices/optional/simulation_tests", SimulationTestOptionalViewSet)
router.register("prices/optional/facebook_private_groups", FacebookPrivateGroupOptionalViewSet)
router.register("prices/optional/external_courses", ExternalCourseOptionalViewSet)
router.register("prices/optional/external_exams", ExternalExamOptionalViewSet)
router.register("prices/optional/support_sales", SupportSaleOptionalViewSet)
router.register("prices/optional/packagings", PackagingOptionalViewSet)
router.register("prices/optional/course_edugadgets", CourseEduGadgetOptionalViewSet)
router.register("prices/optional/gifts", GiftOptionalViewSet)


# Product Groups
router.register("product_groups/product_groups", ProductGroupViewSet)


# Product Types
router.register("product_types/course_books", CourseBookViewSet)
router.register("product_types/course_bundles", CourseBundleViewSet)
router.register("product_types/course_services", CourseServiceViewSet)
router.register("product_types/courses", CourseViewSet)
router.register("product_types/e_documents", EDocumentViewSet)
router.register("product_types/edugadget_bundles", EduGadgetBundleViewSet)
router.register("product_types/edugadgets", EduGadgetViewSet)
router.register("product_types/simulation_tests", SimulationTestViewSet)
router.register("product_types/external_courses", ExternalCourseViewSet)
router.register("product_types/external_exams", ExternalExamViewSet)
router.register("product_types/support_sales", SupportSaleViewSet)
router.register("product_types/facebook_private_groups", FacebookPrivateGroupViewSet)
router.register("product_types/course_edugadgets", CourseEduGadgetViewSet)
router.register("product_types/gifts", GiftViewSet)


# Products
router.register("products/products", ProductViewSet)
router.register("products/product_images", ProductImageItemViewSet)
router.register("products/bundle_sets", BundleSetViewSet)
router.register("products/bundle_set_items", BundleSetItemViewSet)


# Basic API
# LMS
# Odoo
# https://docs.google.com/spreadsheets/d/17EFIHtbsmXgbSbKuhBJzOUlmSKkG7yXCa6HzTXSdh9w/edit#gid=0


# MMS
# FMS
# CRM
# https://docs.google.com/spreadsheets/d/13oTFF_S_8fwqjP8R50PsU3s6xgNIz4VJ0pO9suP1KNo/edit#gid=716653789


app_name = "api"
urlpatterns = router.urls
