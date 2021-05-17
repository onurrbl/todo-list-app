from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# from django.contrib.sessions.models import Session
# Create your models here.


class ToDo(models.Model):
    IMPORTANCY_LEVEL_CHOICES = [
        ('Regular','regular'),
        ('Important','important')
    ]
    user = models.ForeignKey(User ,null=True,blank=True, on_delete=models.CASCADE,related_name='todos')
    todo_title = models.CharField(max_length=200, null=True ,blank=True)
    todo_text = models.CharField(max_length=200, null=True, blank=True)
    expire_date = models.DateField(null=True, blank=True)
    importancy_level = models.CharField(max_length=20,choices=IMPORTANCY_LEVEL_CHOICES,default= 'Regular')
    is_accomplished = models.BooleanField(null = True , blank = True , default=False)