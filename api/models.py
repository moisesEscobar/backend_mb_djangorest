from django.db import models
from django.utils import timezone
from datetime import datetime, timezone
from django.conf import settings

class User(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    second_surname = models.CharField(max_length=255, blank=True, null=True)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = "users"