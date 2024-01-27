from django.shortcuts import render
from todo.models import Task

def home(request):
    incompleted_tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)
    context = {
        'incompleted_tasks': incompleted_tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'home.html', context)