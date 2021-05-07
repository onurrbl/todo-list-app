from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class ToDo(models.Model):
    user = models.ForeignKey(get_user_model(),null=True,blank=True, on_delete=models.SET_NULL,related_name='todos')
    todo_title = models.CharField(max_length=200, null=True ,blank=True)
    todo_parameter = models.CharField(max_length=200, null=True, blank=True)
    expire_date = models.DateField(null=True, blank=True)
    