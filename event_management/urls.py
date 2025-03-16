from django.contrib import admin
from django.urls import path, include
from events.views import home, about, contact_us, dashboard, all_events


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact-us/', contact_us, name='contact_us'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/all-events', all_events, name='all-events'),
    path('events/', include("events.urls")),
]
