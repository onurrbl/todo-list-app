from django.shortcuts import render
from django.http import (
    HttpResponse,
    
)
# Create your views here.



def homeView(request,*args,**kwargs):


    return render(request,'base.html', { } )