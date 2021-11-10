from django.shortcuts import render, redirect
from django.contrib import messages

from api.models import TodoNote
from .forms import TodoForm

# Create your views here.


def index(request):
    current_user = request.user
    complete_todos = TodoNote.objects.filter(complete='Yes').all()
    incomplete_todos =TodoNote.objects.filter(complete='No').all()

    context = {
        'complete_todos': complete_todos,
        'incomplete_todos': incomplete_todos

    }
    return render(request, 'index.html', context)


def add_todo(request):
    if request.method == 'POST':
        add_todo_form = TodoForm(request.POST)
        if add_todo_form.is_valid():
            todo = add_todo_form.save(commit=False)
            todo.save()
            
            messages.success(request, f'New todo added!')
            return redirect('todo_app:index')

    else:
        add_todo_form = TodoForm()

    return render(request, 'add_todo.html', {'add_todo_form': add_todo_form})

def todo_details(request, todo_id):
    todo = TodoNote.objects.get(pk=todo_id)

    return render(request, 'todo_page.html', {'todo': todo})


def update_todo(request, todo_id):
    todo = TodoNote.objects.get(pk=todo_id)

    if request.method == 'POST':
        update_todo_form = TodoForm(request.POST, instance=todo)
        if update_todo_form.is_valid():
            update_todo_form.save()
            messages.success(request, f'Todo updated!')
            return redirect('todo_app:index')
    else:
        update_todo_form = TodoForm(instance=todo)
    context = {
        "update_todo_form": update_todo_form,
        "todo": todo
    }
    return render(request, 'update_todo.html', context)


def delete_todo(request, todo_id):
    todo = TodoNote.objects.get(pk=todo_id)
    if todo:
        todo.delete_todo()
        messages.success(request, f'Todo deleted!')
    return redirect('todo_app:index')

def search(request):
  if 'todo' in request.GET and request.GET["todo"]:
    search_term = request.GET.get("todo")
    searched_todos = TodoNote.search_todos(search_term)
    message = f"{search_term}"

    return render(request,'search.html', {"message":message,"todos":searched_todos})

  else:
    message = "You haven't searched for any term"
    return render(request,'search.html',{"message":message})
