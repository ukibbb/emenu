from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

API_VERSION = "api/v1/"

urlpatterns = [
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
        include(("accounts.urls", "accounts"), namespace="accounts"),
    ),
    path(
        f"{API_VERSION}menus/", include("menus")
    )
    path("admin/", admin.site.urls),
]
