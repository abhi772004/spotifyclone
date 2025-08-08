from django.shortcuts import render
from django.views import View
from .models import *



class home(View):
    def get(self, request):
        # Fetch all songs from the database in a list called 'songs'
        songs = Song.objects.all() 
        # Create a dictionary to pass the songs to the template
        context = {'songs': songs}
        # Render the 'index.html' template with the song data
        return render(request, 'home.html', context)