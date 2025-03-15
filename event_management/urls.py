from django.contrib import admin
from django.urls import path, include
from events.views import home, about, contact_us


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact-us/', contact_us, name='contact_us'),
    path('events/', include("events.urls")),
]
