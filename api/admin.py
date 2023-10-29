from django.contrib import admin

from api.models import Specialization, Visit, Patient, Service, Schedule

# Register your models here.

admin.site.register(Specialization)
admin.site.register(Visit)
admin.site.register(Patient)
admin.site.register(Service)
admin.site.register(Schedule)