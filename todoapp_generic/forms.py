from . models import Task_list
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model=Task_list
        fields=['name','priority','date']
