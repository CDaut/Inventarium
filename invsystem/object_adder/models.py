from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.

class Object(models.Model):
    ammout = models.PositiveIntegerField(default=1, blank=False)
    title = models.TextField(max_length=100, default=None, blank=False)
    img = models.ImageField(default=None, blank=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inventarized_date = models.DateTimeField(blank=False, null=True)
    description = models.TextField(max_length=500, blank=True)
    removed_date = models.DateTimeField(blank=True, default=None, null=True)
    user_added = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, default=None, null=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.uuid)


class Category(models.Model):
    name = models.TextField(blank=False, max_length=150)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    categories = models.Manager()

    def __str__(self):
        return self.name
