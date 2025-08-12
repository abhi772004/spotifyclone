from django.shortcuts import render
from django.views import View
from .models import Artist,Song



# class home(View):
#     def get(self, request):
#         # Fetch all songs from the database in a list called 'songs'
#         songs = Song.objects.all() 
#         artists=Artist.objects.prefetch_related('songs').all()
#         artists_data = []
#         for artist in artists:
#             artists_data.append({
#                 'id': artist.id,
#                 'name': artist.name,
#                 'image_url': artist.image.url if artist.image else '',
#                 'verified': artist.verified,
#                 'songs': [{'title': song.title, 'album_art_url': song.album_art.url if song.album_art else ''} for song in artist.songs.all()]
#             })

#         context = {'songs': songs, 'artists': artists, 'artists_data': artists_data}
#         # Render the 'index.html' template with the song data
#         return render(request, 'home.html', context)
    


    
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Artist, Song

class home(View):
    def get(self, request, artist_id=None):
        context = {}
        
        if artist_id:
            # Logic for the artist detail page
            artist = get_object_or_404(Artist, pk=artist_id)
            songs_by_artist = artist.songs.all()
            
            context['artist'] = artist
            context['songs_by_artist'] = songs_by_artist
            context['is_detail_page'] = True
        else:
            # Logic for the main home page
            songs = Song.objects.all()
            artists = Artist.objects.all()
            
            # Pre-fetching songs for the home page (as in your original code)
            artists_data = []
            for artist_obj in artists:
                artists_data.append({
                    'id': artist_obj.id,
                    'name': artist_obj.name,
                    'image_url': artist_obj.image.url if artist_obj.image else '',
                    'verified': artist_obj.verified,
                    'songs': [{'title': song.title, 'album_art_url': song.album_art.url if song.album_art else ''} for song in artist_obj.songs.all()]
                })

            context['songs'] = songs
            context['artists'] = artists
            context['artists_data'] = artists_data
            context['is_detail_page'] = False

        return render(request, 'home.html', context)




