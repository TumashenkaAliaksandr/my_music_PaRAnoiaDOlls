from django.shortcuts import render

from webapp.models import Song, Concert


def index(request):
    return render(request, 'webapp/index.html')

def about(request):
    songs = Song.objects.all()
    context = {
        'songs': songs,
    }
    return render(request, 'webapp/about.html', context=context)

def concerts(request):
    concerts = Concert.objects.all()
    context = {
        'concerts': concerts,
    }
    return render(request, 'webapp/gallery.html', context=context)

def events(request):
    return render(request, 'webapp/events.html')

def eventsdat(request):
    return render(request, 'webapp/events-detail.html')

def tests_one(request):
    return render(request, 'webapp/tests.html')