from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import  *
from django.views.generic import ListView

class home(View):
    def get(self, request):
        songs = Song.objects.all()
        return render(request, 'home.html', {'songs': songs})


    
    
    

 
 

# class songview(ListView):
#    model = Song
#    template_name = 'content/song_list.html'
#    context_object_name = 'songs'

#    def get_queryset(self):
#        return Song.objects.select_related('artist').all()

