from django.shortcuts import render

def index(request):
    return render(request, 'webapp/index.html')

def about(request):
    return render(request, 'webapp/aboutus.html')

def gallery(request):
    return render(request, 'webapp/gallery.html')

def events(request):
    return render(request, 'webapp/events.html')

def eventsdat(request):
    return render(request, 'webapp/events-detail.html')

def tests_one(request):
    return render(request, 'webapp/tests.html')