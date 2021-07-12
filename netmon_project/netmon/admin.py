from django.contrib import admin
from .models import Device, Alert

# Register your models here.
admin.site.register(Device)
admin.site.register(Alert)