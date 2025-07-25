from django import forms
from task_event.models import Event, Category, Participant


class EventForm(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    location = forms.CharField(max_length=200)
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    def save(self, commit=True):
        data = self.cleaned_data
        event = Event(
            name=data['name'],
            description=data['description'],
            date=data['date'],
            time=data['time'],
            location=data['location'],
            category=data['category'],
        )
        if commit:
            event.save()
        return event

class ParticipantForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    events = forms.ModelMultipleChoiceField(queryset=Event.objects.all(), widget=forms.CheckboxSelectMultiple)

    def save(self, commit=True):
        data = self.cleaned_data
        participant = Participant(
            name=data['name'],
            email=data['email'],
        )
        if commit:
            participant.save()
            participant.events.set(data['events'])
        return participant


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)

    def save(self, commit=True):
        data = self.cleaned_data
        category = Category(
            name=data['name'],
            description=data['description'],
        )
        if commit:
            category.save()
        return category