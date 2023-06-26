from webapp.models import Song, Concert, News, Merchandise, TShirt, Cap
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView
from webapp.forms import RegisterUserForm
from .forms import SubscriptionForm
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from .models import Subscription
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    """Main, about band"""
    merch = Merchandise.objects.all()
    main_merch = Merchandise.objects.filter(is_main=True).first()
    main_concerts = Concert.objects.all()

    context = {
        'merch': merch,
        'main_merch': main_merch,
        'main_concerts': main_concerts,
    }
    return render(request, 'webapp/index.html', context=context)


def music_about(request):
    """Views name: Band Songs"""
    songs = Song.objects.all()
    main_concerts = Concert.objects.all()
    context = {
        'songs': songs,
        'main_concerts': main_concerts,
    }
    return render(request, 'webapp/music.html', context=context)


def concert(request):
    """Views name: Band Concert"""
    concerts = Concert.objects.all()
    context = {
        'concerts': concerts,

    }
    return render(request, 'webapp/gallery.html', context=context)


def events(request):
    """Views name: Band Merch"""
    merchandise = Merchandise.objects.all()
    paginator = Paginator(merchandise, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tshirts = TShirt.objects.all()
    caps = Cap.objects.all()
    context = {
        'page_obj': page_obj,
        'merchandise': merchandise,
        'tshirts': tshirts,
        'caps': caps,
    }
    return render(request, 'webapp/events.html', context)


def eventsdat(request):
    """these are views for booking the event"""
    return render(request, 'webapp/events-detail.html')


def tests_one(request):
    """this is views for tests"""
    return render(request, 'webapp/tests.html')


class NewsListView(ListView):
    """these are views for News list"""
    model = News
    template_name = 'blog/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 5
    ordering = ['-pub_date']

    # def get_context_data(self, **kwargs):
    #     """for paginations"""
    #     context = super().get_context_data(**kwargs)
    #     paginator = context['paginator']
    #     page_numbers_range = 5
    #     max_index = len(paginator.page_range)
    #     current_page = context['page_obj'].number
    #     start_index = current_page - page_numbers_range if current_page > page_numbers_range else 0
    #     end_index = current_page + page_numbers_range if current_page < max_index - page_numbers_range else max_index
    #     context['page_range'] = list(paginator.page_range[start_index:end_index])
    #     return context


class CRLoginView(LoginView):
    """create login"""
    template_name = 'webapp/login.html'
    redirect_authenticated_user = True


class CRLogoutView(LoginRequiredMixin, LogoutView):
    """logout views"""
    template_name = 'webapp/index.html'
    next_page = reverse_lazy('webapp:home')


class RegisterUserView(CreateView):
    """Registration"""
    model = User
    template_name = 'webapp/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('webapp:register_done')


class RegisterDoneView(TemplateView):
    """Confirmation of registration"""
    template_name = 'webapp/register_done.html'


# def subscribe(request):
#     if request.method == 'POST':
#         form = SubscriptionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'webapp/success.html')
#     else:
#         form = SubscriptionForm()
#     return render(request, 'webapp/subscribe.html', {'form': form})

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Subscription.objects.filter(email=email).exists():
                return render(request, 'webapp/already_subscribed.html')
            else:
                confirmation_code = get_random_string(length=32)  # Генерация уникального кода подтверждения
                subscription = Subscription(email=email, confirmation_code=confirmation_code)
                subscription.save()

                # Генерация ссылки подтверждения
                confirmation_url = request.build_absolute_uri(
                    reverse('webapp:confirm_subscription', kwargs={'confirmation_code': confirmation_code}))

                # Отправка письма
                subject = 'Подтверждение подписки'
                message = f'Для подтверждения подписки, перейдите по ссылке: {confirmation_url}'
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]

                send_mail(subject, message, from_email, recipient_list)

                return render(request, 'webapp/success.html')
    else:
        form = SubscriptionForm()
    return render(request, 'webapp/subscribe.html', {'form': form})

