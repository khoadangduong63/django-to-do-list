# TO DO LIST APPLICATION


## 1. Link course
* https://fpt-software.udemy.com/course/python-django-real-world-project-multi-vendor-restaurant/learn/lecture/37719378#overview
* In section 2: Django Refresher For Beginners


## 2. Create project
```bash
$ python manage.py startproject todo_main .
```
* Note: If not have "." end of statement, django will create new folder with same name project and give project inside it


## 3. Migrate database
```bash
$ python manage.py migrate
```


## 4. Create supper user
```bash
$ python manage.py createsupperuser
```


## 5. Create HomeView
* Step 1: Add path into todo_main/urls.py of project
```python
from django.contrib import admin
from django.urls import path
from . import views # It's here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # It's here
]
```

* Step 2: Create file views.py into todo_main
```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

* Step 3: Create folder templates in root directory (same level with todo_main), create `home.html` inside it
* Step 4: Add path of folder `templates` at field `TEMPLATES`/`DIRS` in file `settings.py`


## 6. Create app
* Step 1: Enter command line with name of app as `todo`
```bash
$ python manage.py startapp todo
```

* Step 2: Declare app `todo` at field `INSTALLED_APPS` in file `settings.py`
* Step 3: Define a model `Task` in `todo/models.py`
```python
from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)

    # Recommend to use for every model, because it's very important while storing the big data in database.
    # Can see when data was created and modified previously
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Set a string representation of this model
    def __str__(self):
        return self.task
```

* Step 4: Register model inside `todo/admin.py`
```python
from django.contrib import admin
from .models import Task

# Register your models here.
admin.site.register(Task)
```

* Step 5: Enter command line to makemigrate and migrate new model to database (Very important when define new model)
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```
* Note: If not have this step, it'll return error when click to Task in Admin Page (http://127.0.0.1:8000/admin/). Because cannot find that model.


## 7. Create logic code to fectch tasks from database and show on UI
* Step 1: Create incompleted and completed tasks on Admin Page
* Step 2: Edit logic code in `todo_main/views.py` and `templates/home.html`


## 8. Create TaskAdmin to manage tasks
* Create class `TaskAdmin` is inherited from `admin.ModelAdmin` in file `todo/admin.py`
```python
from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'created_at', 'updated_at')
    search_fields = ('task',)

admin.site.register(Task, TaskAdmin)
```


## 9. Create add_task function and activate CSRF token
* Step 1: Define path in `todo_main/urls.py`
* Step 2: In `todo`, create new file `urls.py` and add an API
* Step 3: In `todo/views.py`, create function is called by `todo/urls.py`
* Step 4: Change some fields to get data from form
* Step 5: Activate CSRF token to secure (Very important, always activate CSRF token with POST method)


## 10. Mark as done
* Step 1: Add API `mark-as-done` in `todo/urls.py`
* Step 2: In `todo/views.py`, create function is called by `todo/urls.py`
* Step 3: In file `templates/home.html`, at anchor tag which has `href`, add name of API here
```html
<a href="{% url 'mark_as_done' incompleted_task.pk %}" class="btn btn-success"><i class="fa fa-check"></i> Mark as Done</a>
```


## 11. Edit task
* Step 1: Add API `edit_task` in `todo/urls.py`
* Step 2: In `todo/views.py`, create function is called by `todo/urls.py`
* Step 3: In file `templates/home.html`, at anchor tag which has `href`, add name of API here
* Step 4: In `edit_task` function, define 2 logic, one for GET method to get info current task, other for POST method to assign value new task to current task for updating purpose
```python
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
```
* Step 5: Create `templates/edit_task.html`