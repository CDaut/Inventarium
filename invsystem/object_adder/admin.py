from django.contrib import admin
from .models import Object


class ObjectAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Object, ObjectAdmin)
