from django.shortcuts import render, redirect
from todo.forms import TaskForm
from todo.models import TaskModel


# Create your views here.

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incompleted_tasks')
    else:
        form = TaskForm()
    return render(request, 'add_and_update_task.html', {'form': form})

def incomplete_tasks(request):
    tasks = TaskModel.objects.filter(is_completed=False)
    return render(request, 'incomplete.html', {'tasks': tasks})

def update_task(request, task_id):
    task = TaskModel.objects.get(pk = task_id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('incompleted_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'add_and_update_task.html', {'form': form})

def completed_tasks(request):
    tasks = TaskModel.objects.filter(is_completed=True)
    return render(request, 'completed_tasks.html', {'tasks': tasks})

def mark_completed(request, task_id):
    task = TaskModel.objects.get(pk = task_id)
    task.is_completed = True
    task.save()
    return redirect('completed_tasks')

def delete_task(request, task_id):
    TaskModel.objects.get(pk=task_id).delete()
    return redirect('incompleted_tasks')

