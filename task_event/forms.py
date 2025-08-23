from django import forms
from task_event.models import Event, Category, Participant
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'description': forms.Textarea(),
        }

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
    
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user