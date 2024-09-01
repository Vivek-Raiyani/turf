from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Facility)
admin.site.register(FacilityLocation)
admin.site.register(FacilityType)
admin.site.register(Review)