from django.db import models
from django.utils import timezone

class Books(models.Model):
    Name = models.CharField(max_length=100)
    Page_Number = models.CharField(max_length=200)
    Genre = models.CharField(max_length=50)
    pub_date = models.Field(default=timezone.now)
