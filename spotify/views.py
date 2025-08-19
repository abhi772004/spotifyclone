from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import  *
from django.views.generic import ListView

class home(View):

 def get(self, request):
    return render(request, 'home.html')
 

 
 

class songview(ListView):
   model = Song
   template_name = 'content/song_list.html'
   context_object_name = 'songs'

   def get_queryset(self):
       return Song.objects.select_related('artist').all()

