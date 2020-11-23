from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from .models import task, Person
from .form import TaskForm

# Create your views here.
def TaskListView(request):
    taskList = task.objects.all()
    context = {
        'taskList': taskList
        }
    return render(request, 'task/task_list.html', context)

def TaskDetailView(request, id):
    if request.method == 'POST':
        task_exist = task.objects.filter(id=id).exists()
        if task_exist:
            task_item = task.objects.get(id=id)
            form = TaskForm(request.POST, instance=task_item)
        else:
            form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_veiw_url')
    elif request.method == 'GET':  
        task_item = get_object_or_404(task, id=id)
        form = TaskForm(instance=task_item)
    else:
        form = TaskForm()
    method = 'update'
    return render(request, 'task/task_detail.html', {'form': form, 'task_item': task_item, 'method': method})

def TaskCreateView(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_veiw_url')
    
    form = TaskForm()
    method = 'create'
    return render(request, 'task/task_detail.html', {'form': form, 'method': method})


class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'job_title', 'bio')