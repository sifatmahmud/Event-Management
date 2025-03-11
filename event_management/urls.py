from django.contrib import admin
from django.urls import path, include
from events.views import home, about


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('events/', include("events.urls")),
]
