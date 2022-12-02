from django.db import models
from datetime import datetime

class Media(models.Model):
    name = models.CharField(max_length=15)
    datetime_process = models.DateTimeField(default = datetime.now())
    process_type = models.CharField(max_length=8000, default='')

    def __str__(self):
        return self.name