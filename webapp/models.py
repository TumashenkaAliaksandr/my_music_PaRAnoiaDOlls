from django.db import models
from django.urls import reverse


class Song(models.Model):
    """Song model"""
    title = models.CharField(max_length=100)
    albums = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='song_photos/', blank=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})