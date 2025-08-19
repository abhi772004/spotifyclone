from django.db import models

# Create your models here.


class Artist(models.Model):
    name=models.CharField(max_length=100,null=True, blank=True)
    image=models.ImageField(upload_to='artists/',null=True, blank=True)

    def __str__(self):
     return self.name

class Song(models.Model):
    artist=models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    title=models.CharField(max_length=100,null=True, blank=True)
    songimg=models.ImageField(upload_to='songs/',null=True, blank=True)
    audio=models.FileField(upload_to='songs/',null=True, blank=True)

    def __str__(self):
      return self.title

