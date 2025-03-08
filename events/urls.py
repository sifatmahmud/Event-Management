from django.urls import path
from events.views import create_event, create_category, create_participant, update_event

urlpatterns = [
    path('create-event/', create_event, name='create-event'),
    path('create-category/', create_category, name='create-category'),
    path('create-participant/', create_participant, name='create-participant'),
    path('update-event/<int:event_id>/', update_event, name='update-event'),

]
