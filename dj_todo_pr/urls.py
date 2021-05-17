"""dj_todo_pr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todocomp.views import Logout_func, home_View, login_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_View),
    path('register/',register_view, name= 'register_view'),
    path('login/',login_view),
    path('logout/', Logout_func),
    path('todo/', include('todocomp.urls')),
]
