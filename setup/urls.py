from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from model_manager.views import MediasViewSet

router = routers.DefaultRouter()
router.register('medias', MediasViewSet, basename='model_manager')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
