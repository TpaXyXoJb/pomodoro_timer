from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import TaskCreationForm, TaskUpdateForm, LoopCreateForm

from .models import Task, Loop


class TasksView(ListView):
    model = Task
    queryset = Task.objects.all()
    template_name = 'task/task_list.html'


class TaskDetailView(DetailView):
    model = Task
    queryset = Task.objects.all()
    template_name = 'task/task_detail.html'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task/task_new.html'
    form_class = TaskCreationForm
    success_url = reverse_lazy('home')


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task/task_edit.html'
    form_class = TaskUpdateForm
    success_url = reverse_lazy('home')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task/task_delete.html'
    success_url = reverse_lazy('home')


class LoopDetailView(DetailView):
    model = Loop
    queryset = Loop.objects.all()
    template_name = 'loop/loop_detail.html'


class LoopCreateView(CreateView):
    model = Loop
    template_name = 'index.html'
    form_class = LoopCreateForm


class LoopUpdateView(UpdateView):
    model = Loop
    template_name = 'loop/loop_edit.html'
    fields = ['is_started', 'is_finished']


class LoopDeleteView(DeleteView):
    model = Loop
    template_name = 'loop/loop_delete.html'
    success_url = reverse_lazy('home')


def delete_loops(request):
    Loop.objects.get(is_finished=True).delete()
    return redirect('home')


def delete_tasks(request):
    Task.objects.all().delete()
    return redirect('home')


