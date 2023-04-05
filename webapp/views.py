from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from webapp.models import Song, Concert, News


def index(request):
    return render(request, 'webapp/index.html')


def about(request):
    songs = Song.objects.all()
    context = {
        'songs': songs,
    }
    return render(request, 'webapp/about.html', context=context)


def concert(request):
    concerts = Concert.objects.all()
    context = {
        'concerts': concerts,
    }
    return render(request, 'webapp/news_list.html', context=context)


def events(request):
    return render(request, 'webapp/events.html')


def eventsdat(request):
    return render(request, 'webapp/events-detail.html')


def tests_one(request):
    return render(request, 'webapp/tests.html')


class NewsListView(View):
    def get(self, request):
        news_list = News.objects.all()
        paginator = Paginator(news_list, 5)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'webapp/news_list.html', {'page_obj': page_obj})