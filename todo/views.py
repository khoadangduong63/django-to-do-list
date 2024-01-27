from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

# Create your views here.
def add_task(request):
    new_task = request.POST.get('new_task')
    if new_task is not None and new_task != '' and Task.objects.filter(task=new_task).exists() == False:
        Task.objects.create(task=new_task)
    return redirect('home')


def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')


def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        updated_task = request.POST.get('updated_task')
        task.task = updated_task
        task.save()
        return redirect('home')
    else:
        context = {
            'task': task
        }
    return render(request, 'edit_task.html', context)


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')