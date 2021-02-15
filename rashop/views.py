from django.shortcuts import render, redirect
from .models import Todo
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


def index(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    return render(request, 'index.html', {'todo_items': todo_items})


def add_todo(request):
    content = request.POST['content']
    current_time = timezone.now()
    created_object = Todo.objects.create(added_date=current_time, text=content)
    return redirect('/')


@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')