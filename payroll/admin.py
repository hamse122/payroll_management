# payroll/admin.py

from django.contrib import admin
from .models import *

admin.site.register(Payroll)
admin.site.register(Contact)
