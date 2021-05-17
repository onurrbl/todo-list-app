from django.urls import path
from .views import(

    delete_todo,
    add_todo_view,
    home_View,
    edit_todo_view,

)

app_name = 'todocomp'
urlpatterns = [

    path('home/', home_View , name = 'homeview'),
    path('add-todo/', add_todo_view, name = 'addtodoview'),
    path('edit-todo/<int:todo_id>/', edit_todo_view, name='edittodoview'),
    path('delete-todo/<int:todo_id>/',delete_todo, name= 'deletetodo'),

]