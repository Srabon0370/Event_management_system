from django.urls import path
from task_event.views import say_hello

urlpatterns = [
    path('saif/', say_hello, name='saif')
]
