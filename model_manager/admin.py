from django.contrib import admin
from model_manager.models import Media
class Medias(admin.ModelAdmin):
    list_display = ('id', 'name', 'datetime_process', 'process_type')
    list_display_links = ('id', 'name', 'datetime_process', 'process_type')
    search_fields = ('id', 'name', 'datetime_process', 'process_type')
    list_per_page = 20

admin.site.register(Media, Medias)