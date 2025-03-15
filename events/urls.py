from django.urls import path
from events.views import create_event, create_category, create_participant, event_detail, events_list

urlpatterns = [
    path('create-event/', create_event, name='create-event'),
    path('create-category/', create_category, name='create-category'),
    path('create-participant/', create_participant, name='create-participant'),
    path('<int:event_id>/', event_detail, name='event_detail'),
    path('', events_list, name='events_list'),
]
