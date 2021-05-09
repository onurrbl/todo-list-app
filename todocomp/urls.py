from django.urls import path
from .views import(
    homeView,
    add_todo_view,

)


urlpatterns = [

    path('home/', homeView ),
    path('add-todo/', add_todo_view),
]