from django.contrib import admin
from app.models import EmployeeData
# Register your models here.
@admin.register(EmployeeData)
class Emp_Admin(admin.ModelAdmin):
    list_display=['name','age','domain']

