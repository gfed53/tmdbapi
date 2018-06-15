import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class CachedList(models.Model):
  name = models.CharField(max_length=200)
  list_data = models.TextField()
  date_updated = models.DateTimeField()

  def __str__(self):
    return self.name