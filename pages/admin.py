from django.contrib import admin
from .models import Entertainment
# Register your models here.
class ListEnt(admin.ModelAdmin):
    list_display = ('id', 'title','category')
    list_display_links = ('id', 'title')
    list_filter = ('category',)
    search_fields = ('title', 'description')
    list_per_page = 30
admin.site.register(Entertainment,ListEnt)
