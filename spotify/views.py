from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .models import Song, Artist, Album


# Home Page - cache for 30s
@method_decorator(cache_page(30), name='dispatch')
class home(View):
    def get(self, request):
        print("⚡ Fetching songs, artists, albums from DB...")  # Debug log
        songs = Song.objects.all()
        artists = Artist.objects.all()
        albums = Album.objects.all()
        return render(request, 'home.html', {
            'songs': songs,
            'artists': artists,
            'albums': albums
        })


# Artist Detail - cache for 20s
@method_decorator(cache_page(20), name='dispatch')
class artistview(DetailView):
    model = Artist
    template_name = 'content/artistdetail.html'
    context_object_name = 'artist'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artist = self.object
        context['songs'] = Song.objects.filter(artists=artist)
        print("⚡ Fetching songs for artist from DB...")  # Debug log
        return context


# Album Detail - cache for 20s
@method_decorator(cache_page(20), name='dispatch')
class albumview(DetailView):
    model = Album
    template_name = "content/albumdetail.html"
    context_object_name = "album"
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = self.object
        context["songs"] = Song.objects.filter(album=album)
        print("⚡ Fetching songs for album from DB...")  # Debug log
        return context

from rest_framework import viewsets    
from .models import Song,Album, Artist

from .serializers import AlbumSerializer, ArtistSerializer, SongSerializer

class songViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class albumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class artistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer