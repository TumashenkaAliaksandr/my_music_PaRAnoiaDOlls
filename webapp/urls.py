from django.urls import path
from django.conf.urls.static import static

from my_music import settings
from webapp.views import *

app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('music/', music_about, name='music'),
    path('events/', events, name='events'),
    path('eventsdat/', eventsdat, name='eventsdat'),
    path('concert/', concert, name='concert'),
    path('tests_one/', tests_one, name='tests_one'),

    path('login/', CRLoginView.as_view(), name='login'),
    path('accounts/logout/', CRLogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('accounts/regitster/done/', RegisterDoneView.as_view(), name='register_done'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)