from django.urls import path
from django.conf.urls.static import static

from my_music import settings
from webapp.views import *

app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('events/', events, name='events'),
    path('eventsdat/', eventsdat, name='eventsdat'),
    path('concerts/', concerts, name='concerts'),
    path('tests_one/', tests_one, name='tests_one'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)