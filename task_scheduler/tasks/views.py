from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Tasks
from .forms import TaskForm
import csv


@login_required(login_url='user-login')
def home(request):
    """
    Renders the user's task list on the home page and handles task creation and searching.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered page displaying the user's tasks.
    """
    if request.GET.get('search'):
        search = request.GET.get('search')
        searched_tasks = Tasks.objects.filter(task_name__icontains=search)
        context = {'main_tasks': searched_tasks}
    else:
        user = request.user
        tasks = Tasks.objects.filter(user=user)
        form = TaskForm()
        if request.method == 'POST':
            Tasks.objects.create(
                user=user,
                task_name=request.POST['task_name'],
                date_deadline=request.POST.get('date_deadline')
            )
            return redirect('home')
        context = {'main_tasks': tasks, 'form': form}
    return render(request, 'tasks/home.html', context)


def task_update(request, pk):
    """
    Allows the user to update a specific task.

    Parameters:
    - request: The HTTP request object.
    - pk: The primary key of the task to be updated.

    Returns:
    - A rendered page for updating the task or a redirection to the home page upon completion.
    """
    tsk = Tasks.objects.get(pk=pk)
    form = TaskForm(instance=tsk)
    context = {'form': form}

    if request.method == 'POST':
        tsk.task_name = request.POST['task_name']
        tsk.date_deadline = request.POST.get('date_deadline')
        tsk.save()
        return redirect('home')

    return render(request, 'tasks/task_update.html', context)


def delete(request, pk):
    """
    Deletes a specific task.

    Parameters:
    - request: The HTTP request object.
    - pk: The primary key of the task to be deleted.

    Returns:
    - Redirects to the home page after deleting the task.
    """
    tsk = Tasks.objects.get(pk=int(pk))
    tsk.delete()
    return redirect('home')


def export_csv(request):
    """
    Exports the user's tasks in CSV format.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A CSV file containing the user's task data.
    """
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['task_name', 'deadline'])

    tasks = Tasks.objects.filter(user=request.user)
    for task in tasks:
        writer.writerow([task.task_name, task.date_deadline])

    return response


def about(request):
    """
    Renders the 'About' page of the application.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered 'About' page.
    """
    return render(request, 'tasks/about.html')
