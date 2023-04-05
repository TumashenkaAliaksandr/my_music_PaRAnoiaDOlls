from django.contrib import admin
from .models import Song, Concert, News


class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'photo', 'is_main')

admin.site.register(Song, SongAdmin)

class ConcertAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'date', 'location', 'price', 'is_main')

admin.site.register(Concert, ConcertAdmin)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ('title', 'description')