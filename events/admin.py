from django.contrib import admin
from .models import Instrument, Musician

class MusicianAdmin(admin.ModelAdmin):
    list_display = ('user',)  # Display the username in the list view
    filter_horizontal = ('instrument',)  # Add a horizontal filter for the 'instrument' field

admin.site.register(Instrument)
admin.site.register(Musician, MusicianAdmin)
