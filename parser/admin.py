from django.contrib import admin

# Register your models here.
from parser.models import MexModel, AdminLastSession, PatternModel

admin.site.register(MexModel)
admin.site.register(AdminLastSession)
admin.site.register(PatternModel)
