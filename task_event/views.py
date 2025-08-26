from django.shortcuts import render, redirect
from django.http import HttpResponse
from task_event.models import Event

def say_hello(request):
    return render(request, 'saif.html', {'name': 'saif'})