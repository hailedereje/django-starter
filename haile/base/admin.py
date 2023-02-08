from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.StudentActivity)
admin.site.register(models.Room)
admin.site.register(models.Topic)
admin.site.register(models.Message)
