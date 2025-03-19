from django.shortcuts import render, redirect
from events.forms import Event_Form, Category_Form, Participant_Form, Contact_Us_Form
from django.contrib import messages
from events.models import Event, Participant, Category, Contact_Us
from django.db.models import Count, Q, Prefetch
from django.utils.timezone import now, timedelta
from django.http import JsonResponse





def home(request):
    query = request.GET.get('q')
    events = Event.objects.select_related("category").prefetch_related(Prefetch("participants")).annotate(participants_count=Count('participants'))

    if query:
        events = events.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        events = events[:8] # prothom 8 ta show korbe

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

def update_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == "POST":
        update_event_form = Event_Form(request.POST, instance=event)
        if update_event_form.is_valid():
            update_event_form.save()
            messages.success(request, "Event Updated Successfully")
            return redirect('all-events') 
    else:
        update_event_form = Event_Form(instance=event)

    return render(request, 'forms/update_event.html', {'update_event_form': update_event_form})

def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    print(event_id)
    if request.method == "POST":
        event.delete()
        messages.success(request, "Event Deleted Successfully")
        return redirect('all-events') 

    else:
        messages.error(request, 'Something went wrong')
        return redirect('all-events')

def event_detail(request, event_id):
    event = Event.objects.select_related("category").prefetch_related("participants").annotate(participants_count=Count('participants')).get(id=event_id)
    return render(request, 'event_detail.html', {'event': event})

def events_list(request):
    query = request.GET.get('q')
    events = Event.objects.select_related("category").annotate(participants_count=Count('participants'))
    
    if query:
        events = events.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'events_list.html', {'events': events})

def all_events(request):
    total_events = Event.objects.select_related("category").prefetch_related(Prefetch("participants")).annotate(participants_count=Count("participants"))

    context = {'total_events':total_events}
    return render(request, 'dashboard/all_events.html', context)

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

def update_category(request, category_id):
    category = Category.objects.get(id=category_id)

    if request.method == 'POST':
        update_category_form = Category_Form(request.POST, instance=category)
        if update_category_form.is_valid():
            update_category_form.save()
            messages.success(request, "Category Updated Successfully")
            return redirect('all-categories')
    else:
        update_category_form = Category_Form(instance=category)

    return render(request, 'forms/update_category.html', {'update_category_form': update_category_form})

def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)

    if request.method == "POST":
        category.delete()
        messages.success(request, "Category Deleted Successfully")
        return redirect('all-categories')

    messages.error(request, "Invalid request method")
    return redirect('all-categories')

def all_categories(request):
    total_categories = Category.objects.annotate(event_count=Count('events'))

    context = {'total_categories':total_categories}
    return render(request, 'dashboard/all_categories.html', context)
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

def update_participant(request, participant_id):
    participant = Participant.objects.get(id=participant_id)

    if request.method == 'POST':
        update_participant_form = Participant_Form(request.POST, instance=participant)
        if update_participant_form.is_valid():
            update_participant_form.save()
            messages.success(request, "Participant Updated Successfully")
            return redirect('all-participants')
    else:
        update_participant_form = Participant_Form(instance=participant)
    
    return render(request, 'forms/update_participant.html', {'update_participant_form': update_participant_form})


def delete_participant(request, participant_id):
    participant = Participant.objects.get(id=participant_id)

    if request.method == "POST":
        participant.delete()
        messages.success(request, "Participant Deleted Successfully")
        return redirect('all-participants')
    else:
        messages.error(request, "Something went wrong")
        return redirect('all-participants') 

def all_participants(request):
    total_participants = Participant.objects.annotate(events_count=Count('events'))

    context = {'total_participants':total_participants}
    return render(request, 'dashboard/all_participants.html', context)

# -------------- Contact Us section ---------------------
def contact_us(request):
    if request.method == 'POST':
        contact_us_form = Contact_Us_Form(request.POST)
        if contact_us_form.is_valid():
            contact_us_form.save()
        
        messages.success(request, "Submitted Successfully")
        return redirect('contact_us')
    else:
        contact_us_form = Contact_Us_Form()
    
    return render(request, 'forms/contact_us.html', {'contact_us_form':contact_us_form})

def delete_contact(request, contact_id):
    contact = Contact_Us.objects.get(id=contact_id)

    if request.method == "POST":
        contact.delete()
        messages.success(request, "Contact Deleted Successfully")
        return redirect('all-contacts')
    else:
        messages.error(request, "Something went wrong")
        return redirect('all-contacts') 

def all_contacts(request):
    total_contacts = Contact_Us.objects.all()

    context = {'total_contacts':total_contacts}
    return render(request, 'dashboard/all_contacts.html', context)

# ---------------- Dashboard section ---------------------

def dashboard(request):


    past_one_week = now() - timedelta(days=7)
    recent_events = Event.objects.filter(date__gte=past_one_week, 
    date__lt=now()).order_by('-date').annotate(participants_count=Count('participants')).select_related("category").prefetch_related("participants")

    total_events = Event.objects.select_related("category").annotate(participants_count=Count('participants'))

    past_events = Event.objects.filter(date__lt=now()).order_by('-date').select_related("category").annotate(participants_count=Count('participants'))

    upcoming_events = Event.objects.filter(date__gte=now()).order_by('date').select_related("category").annotate(participants_count=Count('participants'))



    participants = Participant.objects.all()


    categorys = Category.objects.all()

    context = {'recent_events':recent_events, 'total_events':total_events, 'past_events':past_events,'upcoming_events':upcoming_events ,'participants':participants, 'categorys':categorys}
    return render(request, 'dashboard/main_ui.html', context)



