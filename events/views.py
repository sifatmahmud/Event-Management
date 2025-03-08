from django.shortcuts import render, redirect
from events.forms import Event_Form, Category_Form, Participant_Form
from django.contrib import messages
from events.models import Event, Participant, Category



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

def update_event(request, event_id):
    event = Event.objects.get(id=event_id)

    if request.method == "POST":
        update_event_form = Event_Form(request.POST, instance=event)
        if update_event_form.is_valid():
            update_event_form.save()
            messages.success(request, "Event Updated Successfully")
            # return redirect('event-detail', event_id=event.id)
    else:
        update_event_form = Event_Form(instance=event)

    return render(request, "forms/update_event.html", {"update_event_form": update_event_form})


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