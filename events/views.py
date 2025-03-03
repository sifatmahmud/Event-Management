from django.shortcuts import render
from events.forms import Event_Form




def create_event(request):
    if request.method == 'POST':
        form = Event_Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Event_Form()
    
    return render(request, 'forms/create_event.html', {'form':form})