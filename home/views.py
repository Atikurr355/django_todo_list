from django.shortcuts import render
from .models import Task


# Create your views here.
def home(request):
    context = {'success':False}
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']

        ins=Task(title=title,desc=desc)
        ins.save()
        msg=print("List has added one item!")
        context = {'success':True}

    return render(request, 'home.html',context)


def task(request):
    taskdata = Task.objects.all()
    context={
        'task':taskdata,
    }
    return render(request, 'task.html',context)
