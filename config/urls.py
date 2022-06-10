from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include
from django.urls import path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView


def trigger_error(request):
    division_by_zero = 1 / 0  # noqa F405

# Config for admin
admin.site.enable_nav_sidebar = True  # noqa F405

# Base URLS
urlpatterns = [

    # Translate
    path('i18n/', include('django.conf.urls.i18n')),

    # Django Admin, use {% url 'admin:index' %}
    path("", TemplateView.as_view(template_name='base.html'), name="home"),
    path(settings.ADMIN_URL, admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Module URLS
urlpatterns += [
    # User management
    path("users/", include("apps.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),

    # Products
    path("products/", include("apps.products.urls", namespace="products")),
    path("prices/", include("apps.prices.urls", namespace="prices")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# 3rd Party URLS
urlpatterns += [
    # Health Check
    path('ht/', include('health_check.urls')),

    # Filer
    path('filer/', include('filer.urls')),
]

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("apps.api.urls", namespace="api")),

    # DRF auth token
    path("auth-token/", obtain_auth_token),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),

    # Rest Framework
    path('api-auth/', include('rest_framework.urls')),

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]

    # DebugToolbar
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            path("__debug__/", include(debug_toolbar.urls)),

            # Sentry Debug Test
            path("sentry-debug/", trigger_error)
        ]

    # Django-Silk
    if 'silk' in settings.INSTALLED_APPS:
        urlpatterns += [
            path('admin/silk/', include('silk.urls', namespace='silk')),
        ]
