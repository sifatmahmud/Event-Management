from django.urls import path
from events.views import create_event, create_category, create_participant, event_detail, events_list, contact_us, update_event, delete_event, update_category, delete_category, update_participant, delete_participant

urlpatterns = [
    path('create-event/', create_event, name='create-event'),
    path('update-event/<int:event_id>/', update_event, name='update-event'),
    path('delete-event/<int:event_id>/', delete_event, name='delete-event'),
    path('<int:event_id>/', event_detail, name='event_detail'),
    path('create-category/', create_category, name='create-category'),
    path('update/<int:category_id>/', update_category, name='update-category'),
    path('delete/<int:category_id>/', delete_category, name='delete-category'),
    path('create-participant/', create_participant, name='create-participant'),
    path('update-participant/<int:participant_id>/', update_participant, name='update-participant'),
    path('delete-participant/<int:participant_id>/', delete_participant, name='delete-participant'),
    path('', events_list, name='events_list'),
    
]
