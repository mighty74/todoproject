from django.shortcuts import render
from django.views import generic
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.

class Index(generic.ListView):
    template_name = 'index.html'
    model = TodoModel

class TodoList(generic.ListView):
    template_name = 'list.html'
    model = TodoModel


class TodoDetail(generic.DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoUpdate(generic.UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'content', 'deadline')
    success_url = reverse_lazy('todolist')

class TodoDelete(generic.DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('todolist')

class TodoCreate(generic.CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'content', 'deadline')
    success_url = reverse_lazy('todolist')

