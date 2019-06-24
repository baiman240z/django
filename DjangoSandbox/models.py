from django.db import models
from django.utils import timezone


class Hoge(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    body = models.CharField(max_length=3000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(default=timezone.now)
