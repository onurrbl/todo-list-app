from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class ToDo(models.Model):
    IMPORTANCY_LEVEL_CHOICES = [
        ('Regular','regular'),
        ('Important','important')
    ]
    user = models.ForeignKey(get_user_model() or request.user,null=True,blank=True, on_delete=models.SET_NULL,related_name='todos')
    todo_title = models.CharField(max_length=200, null=True ,blank=True)
    todo_text = models.CharField(max_length=200, null=True, blank=True)
    expire_date = models.DateField(null=True, blank=True)
    importancy_level = models.CharField(max_length=20,choices=IMPORTANCY_LEVEL_CHOICES,default= 'Regular')
    is_accomplished = models.BooleanField(default=False)