from django.shortcuts import render
from django.http import (
    HttpResponse,
    
)
from django.contrib.auth import get_user_model
# Create your views here.



def homeView(request,*args,**kwargs):
    user = get_user_model()
    obj = request.user.todos.all()
    context = { "object" : obj}

    return render(request,'base.html', context)