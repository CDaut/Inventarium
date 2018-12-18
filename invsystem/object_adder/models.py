from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.

class Object(models.Model):
    title = models.TextField(max_length=100, default=None)
    img = models.ImageField(default=None)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inventarized_date = models.DateTimeField()
    description = models.TextField(max_length=500)
    removed_date = models.DateTimeField()
    user_added = models.ForeignKey(User, on_delete=models.CASCADE)
