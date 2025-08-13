from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Artist, Song

class home(View):
    """
    Handles:
    - Main home page (all songs & artists)
    - Artist detail page (songs by a specific artist)
    """

    def get(self, request, artist_id=None):
        # Decide which page to render
        if artist_id:
            return self._artist_detail_page(request, artist_id)
        else:
            return self._home_page(request)

    def _home_page(self, request):
        """Logic for the main home page"""
        songs = Song.objects.all()
        artists = Artist.objects.prefetch_related('songs').all()

        # Prepare artist data for template
        artists_data = [
            {
                'id': artist.id,
                'name': artist.name,
                'image_url': artist.image.url if artist.image else '',
                'verified': artist.verified,
                'songs': [
                    {
                        'title': song.title,
                        'album_art_url': song.album_art.url if song.album_art else ''
                    }
                    for song in artist.songs.all()
                ]
            }
            for artist in artists
        ]

        context = {
            'songs': songs,
            'artists': artists,
            'artists_data': artists_data,
            'is_detail_page': False
        }

        return render(request, 'home.html', context)

    def _artist_detail_page(self, request, artist_id):
        """Logic for artist detail page"""
        artist = get_object_or_404(Artist, pk=artist_id)
        songs_by_artist = artist.songs.all()

        context = {
            'artist': artist,
            'songs_by_artist': songs_by_artist,
            'is_detail_page': True
        }

        return render(request, 'home.html', context)
