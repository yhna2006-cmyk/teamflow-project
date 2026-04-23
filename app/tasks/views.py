from .models import Task, TaskFile
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all().order_by('priority')
    return render(request, 'tasks/home.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save()

            files = request.FILES.getlist('files')

            for f in files:
                TaskFile.objects.create(task=task, file=f)

            return redirect('home')

    else:
        form = TaskForm()

    return render(request, 'tasks/add_task.html', {'form': form})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.priority = request.POST.get('priority')
        task.memo = request.POST.get('memo')
        task.status = request.POST.get('status')
        task.save()

        files = request.FILES.getlist('files')

        for f in files:
            TaskFile.objects.create(task=task, file=f)

    return redirect('home')
