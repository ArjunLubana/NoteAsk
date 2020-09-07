from django.shortcuts import render
from django.views.generic import ListView
from .models import Task

""" def tasks(request):
    return render(request, 'task_home.html') """

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'