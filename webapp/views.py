from django.shortcuts import render
from django.views.generic import ListView
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
    return render(request, 'webapp/gallery.html', context=context)


def events(request):
    return render(request, 'webapp/events.html')


def eventsdat(request):
    return render(request, 'webapp/events-detail.html')


def tests_one(request):
    return render(request, 'webapp/tests.html')


class NewsListView(ListView):
    model = News
    template_name = 'blog/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 5
    ordering = ['-pub_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)
        current_page = context['page_obj'].number
        start_index = current_page - page_numbers_range if current_page > page_numbers_range else 0
        end_index = current_page + page_numbers_range if current_page < max_index - page_numbers_range else max_index
        context['page_range'] = list(paginator.page_range[start_index:end_index])
        return context
