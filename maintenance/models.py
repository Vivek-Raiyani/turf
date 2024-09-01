from django.db import models
from facilities.models import Facility
from django.contrib.auth.models import User
# Create your models here.

class Maintanance(models.Model):
          facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
          maintancance_date=models.DateField(null=True)
          last_maintanance_date=models.DateField(null=True)
          requested_by=models.ForeignKey(User, on_delete=models.CASCADE)
          status=models.BooleanField(default=False)
          reason=models.CharField(max_length=100, null=True)
          