from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from my_music import settings
from webapp import views
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
    path('logout/', auth_views.LogoutView.as_view(template_name='webapp/logout.html'), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('accounts/regitster/done/', RegisterDoneView.as_view(), name='register_done'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('merch/<int:merch_id>/like/', like_merch, name='like_merch'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
