from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Todo
import json
from datetime import datetime
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return HttpResponse("Hello world")

@method_decorator(csrf_exempt, name='dispatch')
class TodoView(View):
    
    def get(self, request):
        todos = Todo.objects.all()
        return HttpResponse(todos)

    @csrf_exempt
    def post(self, request):
        req = json.loads(request.body)
        todo = Todo(task=req["tasks"], created_at=timezone.now())
        todo.save()
        return  HttpResponse(todo.id)

@csrf_exempt
def login(request):
    return HttpResponse("")

@csrf_exempt
def register(request):
    return HttpResponse("")