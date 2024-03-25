from django.contrib import admin

# Register your models here.
from .models import Institusi, Bidang, Unit

admin.site.register(Institusi)
admin.site.register(Bidang)
admin.site.register(Unit)