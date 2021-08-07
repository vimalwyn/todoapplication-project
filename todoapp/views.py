from django.http import HttpResponse
from django.shortcuts import render, redirect
from todoapp.models import Task
from .forms import TodoForm
# Create your views here.



def home(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        name=request.POST.get('task','')
        priority = request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'tasks':tasks})

# def details(request):
    task=Task.objects.all()
#     return render(request,'details.html',{'task':task})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    form=TodoForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task})
