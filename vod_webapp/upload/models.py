from django.db import models


class Audit(models.Model):
    uploaded_file = models.CharField(max_length=100)
    uploaded_by = models.CharField(max_length=255)
    outcome = models.CharField(max_length=255)
    context = models.CharField(max_length=255)

    created_on = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)