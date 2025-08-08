from django.db import models

# Create your models here.


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='songs/')
    album_art = models.ImageField(upload_to='song_images/')

    def __str__(self):
        return self.title