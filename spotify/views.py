from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import  *
from django.views.generic import ListView,DetailView

class home(View):
    def get(self, request):
        songs = Song.objects.all()
        artists = Artist.objects.all()
        albums = Album.objects.all()
        return render(request, 'home.html', {'songs': songs, 'artists': artists, 'albums': albums})


class artistview(DetailView):
    model = Artist
    template_name = 'content/artistdetail.html'
    context_object_name = 'artist'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artist=self.object
        context['songs'] = Song.objects.filter(artists=artist)
        print(context,'ccccccccccccccc')
        return context



class albumview(DetailView):
    model = Album
    template_name = "content/albumdetail.html"
    context_object_name = "album"
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = self.object
        context["songs"] = Song.objects.filter(album=album)
        return context

    