from django.urls import path
from . import views
import uuid

urlpatterns = [
    path('', views.objlist, name='objlist'),
    path('<str:orderstr>', views.objlist, name='objlist_ordered'),
    path('<str:uuid_url>/delete', views.delete, name='del_obj')
]
