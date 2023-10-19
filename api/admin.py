from django import admin
from api.models import Specialization, Visit, Patient, Service
# Register your models here.

admin.site.register(Specialization)
admin.site.register(Visit)
admin.site.register(Patient)
admin.site.register(Service)
