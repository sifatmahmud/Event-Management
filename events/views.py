from django.shortcuts import render
from events.forms import Event_Form, Category_Form, Participant_Form




def create_event(request):
    if request.method == 'POST':
        create_event_form = Event_Form(request.POST)
        if create_event_form.is_valid():
            create_event_form.save()
    else:
        create_event_form = Event_Form()
    
    return render(request, 'create_event.html', {'create_event_form':create_event_form})

def create_category(request):
    if request.method == 'POST':
        create_category_form = Category_Form(request.POST)
        if create_category_form.is_valid():
            create_category_form.save()
    else:
        create_category_form = Category_Form()
    
    return render(request, 'create_category.html', {'create_category_form':create_category_form})

def create_participant(request):
    if request.method == 'POST':
        create_participant_form = Participant_Form(request.POST)
        if create_participant_form.is_valid():
            create_participant_form.save()
    else:
        create_participant_form = Participant_Form()
    
    return render(request, 'create_participant.html', {'create_participant_form':create_participant_form})