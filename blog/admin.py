from django.contrib import admin
from webapp.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date']
    list_filter = ['pub_date']
    search_fields = ['title', 'description']
