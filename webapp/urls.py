from django.urls import path
from django.conf.urls.static import static
from webapp.views import *

app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('events/', events, name='events'),
    path('eventsdat/', eventsdat, name='eventsdat'),
    path('gallery/', gallery, name='gallery'),
    path('tests_one/', tests_one, name='tests_one'),

]