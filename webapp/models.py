from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='song_photos/', blank=True)
    audio = models.FileField(upload_to='song_audio/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Concert(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='concert_photos/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.title
