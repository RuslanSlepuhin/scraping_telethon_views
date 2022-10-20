from django.contrib import admin

# Register your models here.
from parser.models import MexModel, AdminLastSession

admin.site.register(MexModel)
admin.site.register(AdminLastSession)
