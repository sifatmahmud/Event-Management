from django.urls import path
from events.views import create_event, create_category, create_participant

urlpatterns = [
    path('create-event/', create_event, name='create-event'),
    path('create-category/', create_category, name='create-category'),
    path('create-participant/', create_participant, name='create-participant'),
]
