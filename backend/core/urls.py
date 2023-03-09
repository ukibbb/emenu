from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

API_VERSION = "api/v1/"


urlpatterns = []

urlpatterns = [
    path(f"{API_VERSION}schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        f"{API_VERSION}schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        f"{API_VERSION}schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path(
        f"{API_VERSION}token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        f"{API_VERSION}token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path(
        f"{API_VERSION}accounts/",
        include(("accounts.urls", "accounts")),
    ),
    path(
        f"{API_VERSION}menus/",
        include(("menus.urls")),
    ),
    path(
        f"{API_VERSION}menu_items/",
        include(("menu_items.urls")),
    ),
    path("admin/", admin.site.urls),
]
