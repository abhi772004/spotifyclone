from django.db import models

# Create your models here.


class Artist(models.Model):
    name=models.CharField(max_length=100,null=True, blank=True)
    image=models.ImageField(upload_to='artists/',null=True, blank=True)

    def __str__(self):
     return self.name

class Song(models.Model):
    artists=models.ManyToManyField(Artist, related_name='songs')
    title=models.CharField(max_length=100,null=True, blank=True)
    songimg=models.ImageField(upload_to='songs/',null=True, blank=True)
    audio=models.FileField(upload_to='songs/',null=True, blank=True)
    album=models.ForeignKey('Album', on_delete=models.CASCADE, null=True, blank=True)   
    def __str__(self):
      return self.title
    
class Album(models.Model):
   coverimage=models.ImageField(upload_to='albums/',null=True, blank=True)    
   albumname=models.CharField(max_length=100,null=True, blank=True)
   artist=models.ManyToManyField(Artist, related_name='albums')
   def __str__(self):
      return self.albumname
   

