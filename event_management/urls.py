from django.contrib import admin
from django.urls import path, include
from events.views import home, about, contact_us, dashboard, all_events, all_categories, all_participants


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact-us/', contact_us, name='contact_us'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/all-events/', all_events, name='all-events'),
    path('dashboard/all-categories/', all_categories, name='all-categories'),
    path('dashboard/all-participants/', all_participants, name='all-participants'),
    path('events/', include("events.urls")),
]
