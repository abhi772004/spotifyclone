from django.db import models

# Create your models here.


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey('artist', on_delete=models.CASCADE,related_name='songs')
    audio_file = models.FileField(upload_to='songs/')
    album_art = models.ImageField(upload_to='song_images/',null=True, blank=True)

    def __str__(self):
        return self.title
    


class Artist(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='artist_images/',null=True, blank=True)
    verified=models.BooleanField(default=False)


    def __str__(self):
        return self.name

