from django.shortcuts import render, redirect
from events.forms import Event_Form, Category_Form, Participant_Form, Contact_Us_Form
from django.contrib import messages
from events.models import Event, Participant, Category
from django.db.models import Count
from django.utils.timezone import now, timedelta
from django.http import JsonResponse




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


# ---------------- Dashboard section ---------------------

def dashboard(request):


    past_one_week = now() - timedelta(days=7)
    recent_events = Event.objects.filter(date__gte=past_one_week, 
    date__lt=now()).order_by('-date').annotate(participants_count=Count('participants'))

    total_events = Event.objects.annotate(participants_count=Count('participants'))

    past_events = Event.objects.filter(date__lt=now()).order_by('-date')

    upcoming_events = Event.objects.filter(date__gte=now()).order_by('date')



    participants = Participant.objects.all()


    categorys = Category.objects.all()

    context = {'recent_events':recent_events, 'total_events':total_events, 'past_events':past_events,'upcoming_events':upcoming_events ,'participants':participants, 'categorys':categorys}
    return render(request, 'dashboard/main_ui.html', context)

def all_events(request):
    total_events = Event.objects.annotate(participants_count=Count('participants'))

    context = {'total_events':total_events}
    return render(request, 'dashboard/all_events.html', context)

