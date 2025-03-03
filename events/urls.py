from django.urls import path
from events.views import create_event

urlpatterns = [
    path('create/', create_event, name='create_event'),
]
