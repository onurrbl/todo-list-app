from django.shortcuts import render
from django.http import (
    HttpResponse,
    
)
from django.contrib.auth import get_user_model
# Create your views here.



def homeView(request,*args,**kwargs):
    user = request.user
    print(user)
    try:
        obj = request.user.todos.all()
        
    except:
        context = { "object" : None}
        return render(request,'main.html', context )
    context = { "object" : obj}
    
    return render(request,'main.html', context )

def add_todo_view(request,*args,**kwargs):



    return render(request, "add_todo.html", {})