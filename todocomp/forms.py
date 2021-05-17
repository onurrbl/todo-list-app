from django import forms
from .models import ToDo


class TodoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields =('todo_title','todo_text', 'expire_date','importancy_level','is_accomplished')

        widget = {
            'todo_title' : forms.TextInput(attrs= {'class' : 'form-control'} ),
            'todo_text' : forms.TextInput(attrs=  {'class' : 'form-control '}),
            'expire_date' : forms.DateInput(attrs=  {'class' : 'form-control '} ),
            'importancy_level' : forms.Select(attrs=  {'class' : 'form-control '} ),
            'is_accomplished' : forms.Select(attrs= {'class' : 'form-control '} ),

        }



class RegisterForm(forms.Form):
    username = forms.CharField(max_length= 100)
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)




class LoginForm(forms.Form):
    username = forms.CharField(max_length= 100)
    password = forms.CharField(max_length=50)



