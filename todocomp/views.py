from django.shortcuts import render
from django.http import (
    HttpResponse,
    render,
)
# Create your views here.



def homeView(request,*args,**kwargs):


    render(request,'base.html', {} )