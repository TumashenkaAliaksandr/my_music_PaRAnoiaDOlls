from django.contrib import admin
from .models import Song, Concert, News


class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'photo', 'is_main')

admin.site.register(Song, SongAdmin)


class ConcertAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'date', 'location', 'price', 'is_main')
    list_filter = ('date',)
    search_fields = ('title', 'description')

admin.site.register(Concert, ConcertAdmin)

