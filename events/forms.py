from django import forms
from events.models import Event


class Event_Form(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date','time', 'location']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'event_time': forms.TimeInput(attrs={'type': 'time'})
        }

