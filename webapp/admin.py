from django.contrib import admin
from .models import Song, Concert

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'is_main')

admin.site.register(Song, SongAdmin)

class ConcertAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'is_main')

admin.site.register(Concert, ConcertAdmin)
