from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
   list_display = ('title', 'artist')
   search_fields = ('title', 'artist')
   admin.site.register(Artist)
