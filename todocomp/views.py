from django.contrib.auth import login, logout
from django.shortcuts import render,redirect
from django.http import (
    HttpResponse,
    
)

from .forms import TodoForm, RegisterForm, LoginForm
from .models import ToDo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.



def home_View(request,*args,**kwargs):
    if not request.user.is_authenticated:
        return redirect("/login/")
        
    try:
        obj = request.user.todos.all()

    except:
        context = { "object" : None}
        return render(request,'main.html', context )
    context = { "object" : obj}
    
    return render(request,'main.html', context )


def register_view(request, *args, **kwargs):
    context = {'form' : RegisterForm}
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_object = User.objects.create(username = username, email = email , password= password)
            user_object.save()
       
            if user_object is not None:
                login(request, user_object)
                return redirect('/todo/home')
            else:
                print("is None")
    return render(request, 'register.html', context)

def login_view(request, *args, **kwargs):
    context = {'form' : LoginForm}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/todo/home')



    return render(request, 'login.html', context)

def Logout_func(request, *args, **kwargs):
    logout(request)

    return redirect('/todo/home')





@login_required(login_url='/login/')
def add_todo_view(request,*args,**kwargs):
    context ={ 'form' : TodoForm}
    if request.method == "GET":
        return render(request, "add_todo.html", context )

    form = TodoForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)

        obj.user = request.user
    
        obj.save()

        return redirect("/todo/home/")


    return render(request, "add_todo.html", context )


@login_required(login_url='/login/')
def edit_todo_view(request,todo_id, *args,**kwargs):
    instance_get = request.user.todos.get(id = todo_id)
    form_object = TodoForm(instance= instance_get)
    context = {'form' : form_object }
    if request.method == "GET":
        return render(request, 'add_todo.html',context)

    form_object = TodoForm(request.POST, instance= instance_get)
    if form_object.is_valid():
        obj = form_object.save()
        return redirect('/todo/home/')
    



    return render(request, 'add_todo.html', context)

@login_required(login_url='/login/')
def delete_todo(request,todo_id,*args,**kwargs):
    obj = request.user.todos.get(id = todo_id).delete()

    return redirect('/todo/home/')

