from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Vendor)
admin.site.register(Purchase_order)
admin.site.register(Vendor_performance_History)