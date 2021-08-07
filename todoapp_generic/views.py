from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from todoapp_generic.models import Task_list
from django. views.generic.detail import DetailView

# Create your views here.
def index():
    return HttpResponse("hello")

class Tasklistview(ListView):
    model = Task_list
    template_name = 'home.html'
    context_object_name = 'tasks'

class Taskdetailview(DetailView):
    model = Task_list
    template_name = 'base.html'
    context_object_name = 'tasks'