from django.contrib import admin
from .models import SystemSole, User, Report

# Register your models here.


admin.site.register(User)
admin.site.register(SystemSole)
admin.site.register(Report)