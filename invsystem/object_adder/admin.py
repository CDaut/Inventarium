from django.contrib import admin
from .models import Object, Category


class ObjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'ammout', 'uuid', 'img')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


# Register your models here.
admin.site.register(Object, ObjectAdmin)
admin.site.register(Category, CategoryAdmin)
