from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter
from CashApi.views import CreateUserViewsets, CashViewSet 

router = DefaultRouter()
router.register(r"user", CreateUserViewsets)
router.register(r"cash", CashViewSet, basename="cash")

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(),
    name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),
    name='token_refresh'),
]+ router.urls
