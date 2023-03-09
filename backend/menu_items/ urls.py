from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MenuItemViewSet

router = DefaultRouter()
router.register("", MenuItemViewSet)

urlpatterns = [path("", include(router.urls))]
