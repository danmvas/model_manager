from rest_framework import viewsets
from model_manager.models import Media
from model_manager.serializers import MediaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

class MediasViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all().order_by('name')
    serializer_class = MediaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]