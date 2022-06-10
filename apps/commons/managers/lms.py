from django.conf import settings
from django.db import models


class LMSRawDataManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().using(settings.LMS_DATABASE_ROUTE)
