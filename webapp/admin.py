from django.contrib import admin
from .models import Song, Concert, Merchandise, TShirt, Cap, MerchandiseCategory


class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'photo', 'is_main')

admin.site.register(Song, SongAdmin)


class ConcertAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'date', 'location', 'price', 'is_main')
    list_filter = ('date',)
    search_fields = ('title', 'description')

admin.site.register(Concert, ConcertAdmin)


class MerchandiseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity')

class TShirtAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'type')

class CapAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'size', 'brim_type')

admin.site.register(Merchandise, MerchandiseAdmin)
admin.site.register(TShirt, TShirtAdmin)
admin.site.register(Cap, CapAdmin)
admin.site.register(MerchandiseCategory)