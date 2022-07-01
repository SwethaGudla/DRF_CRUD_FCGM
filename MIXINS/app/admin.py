from django.contrib import admin
from app.models import StdModel
# Register your models here.
@admin.register(StdModel)
class StdAdmin(admin.ModelAdmin):
    list_display=['name','age','domain']
