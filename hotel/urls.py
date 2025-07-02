from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, OrderViewSet

router = DefaultRouter()
router.register("users", UserViewSet, basename="user")
router.register("orders", OrderViewSet, basename="order")

urlpatterns = [
    path("", include(router.urls)),
]
