from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event-list'),
    path('event/create/', views.create_event, name='event-create'),
    path('participant/create/', views.create_participant, name='participant-create'),
    path('category/create/', views.create_category, name='category-create'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('search/', views.search_events, name='event-search'),
]
