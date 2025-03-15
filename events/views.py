from django.shortcuts import render, redirect
from events.forms import Event_Form, Category_Form, Participant_Form
from django.contrib import messages
from events.models import Event, Participant, Category
from django.db.models import Count




def home(request):
    events = Event.objects.annotate(participants_count=Count('participants'))[:8]
    return render(request, 'home.html', {"events": events})

def about(request):
    return render(request, 'about.html')

# -------------- Event section ---------------------
def create_event(request):
    if request.method == 'POST':
        create_event_form = Event_Form(request.POST)
        if create_event_form.is_valid():
            create_event_form.save()
        
        messages.success(request, "Event Created Successfully")
        return redirect('create-event')
    else:
        create_event_form = Event_Form()
    
    return render(request, 'forms/create_event.html', {'create_event_form':create_event_form})



def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'event_detail.html', {'event': event})

def events_list(request):
    events = Event.objects.annotate(participants_count=Count('participants'))
    return render(request, 'events_list.html', {'events': events})

# -------------- Category section ---------------------
def create_category(request):
    if request.method == 'POST':
        create_category_form = Category_Form(request.POST)
        if create_category_form.is_valid():
            create_category_form.save()
        
        messages.success(request, "Category Created Successfully")
        return redirect('create-category')
    else:
        create_category_form = Category_Form()
    
    return render(request, 'forms/create_category.html', {'create_category_form':create_category_form})

# -------------- Participant section ---------------------
def create_participant(request):
    if request.method == 'POST':
        create_participant_form = Participant_Form(request.POST)
        if create_participant_form.is_valid():
            create_participant_form.save()
        
        messages.success(request, "Participant Created Successfully")
        return redirect('create-participant')
    else:
        create_participant_form = Participant_Form()
    
    return render(request, 'forms/create_participant.html', {'create_participant_form':create_participant_form})