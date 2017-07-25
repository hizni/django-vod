from django.db import models


class StoredData(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    unique_id = models.CharField(max_length=255)

    last_modified = models.DateTimeField(auto_now = True)
    first_created = models.DateTimeField(auto_now_add = True)