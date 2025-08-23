from django.shortcuts import render, redirect
from django.http import HttpResponse
from task_event.models import Event, Participant, Category
from task_event.forms import EventForm, ParticipantForm, CategoryForm
from django.db.models import Count, Q
from datetime import date
from .forms import SignupForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# Create your views here.

def event_list(request):
    events = Event.objects.select_related('category').prefetch_related('participants')
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event-list')
    else:
        form = EventForm()
    return render(request, 'form.html', {'form': form, 'title': 'Create Event'})

@login_required
def create_participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event-list')
    else:
        form = ParticipantForm()
    return render(request, 'form.html', {'form': form, 'title': 'Add Participant'})

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event-list')
    else:
        form = CategoryForm()
    return render(request, 'form.html', {'form': form, 'title': 'Add Category'})

@login_required
def dashboard(request):
    today = date.today()
    total_events = Event.objects.count()
    total_participants = Participant.objects.count()
    upcoming_events = Event.objects.filter(date__gt=today).count()
    past_events = Event.objects.filter(date__lt=today).count()
    events_today = Event.objects.filter(date=today)
    return render(request, 'dashboard.html', {
        'total_events': total_events,
        'total_participants': total_participants,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'events_today': events_today
    })

def search_events(request):
    query = request.GET.get('q', '')
    results = Event.objects.filter(Q(name__icontains=query) | Q(location__icontains=query))
    return render(request, 'search.html', {'events': results, 'query': query})

@login_required
def update_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return HttpResponse("Event not found.", status=404)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event-list')
    else:
        form = EventForm(instance=event)

    return render(request, 'form.html', {'form': form, 'title': 'Update Event'})

@login_required
def delete_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return HttpResponse("Event not found.", status=404)

    event.delete()
    return redirect('event-list')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect("event-list")
    else:
        form = SignupForm()
    return render(request, "registration/signup.html", {"form": form})