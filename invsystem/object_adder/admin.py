from django.contrib import admin
from .models import Object


class ObjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'ammout', 'uuid', 'img')


# Register your models here.
admin.site.register(Object, ObjectAdmin)
