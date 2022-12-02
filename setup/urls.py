from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from model_manager.views import MediasViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = routers.DefaultRouter()
router.register('medias', MediasViewSet, basename='model_manager')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/token/verify/', TokenVerifyView.as_view(), name='token_verify')
]