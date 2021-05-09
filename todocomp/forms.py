from django import forms
from .models import ToDo


class TodoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields =('todo_title','todo_text', 'expire_date','importancy_level','is_accomplished')

        widgets = {
            'todo_title' : forms.TextInput(attrs= 'class' : )
            'todo_text' : forms.TextInput(attrs= 'class' : )
            'expire_date' : forms.DateField(attrs= 'class' : )
            'importancy_level' : forms.Select(attrs= 'class' : )
            'is_accomplished' : forms.TextInput(attrs= 'class' : )

        }