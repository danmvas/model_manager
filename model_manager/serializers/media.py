from rest_framework import serializers
from model_manager.models import Media

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'name', 'datetime_process', 'process_type']
