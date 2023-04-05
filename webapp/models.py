from datetime import datetime

from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    album = models.CharField(max_length=200, verbose_name='Альбом')
    photo = models.ImageField(upload_to='song_photos/', blank=True, verbose_name='Фото')
    audio = models.FileField(upload_to='song_audio/', verbose_name='Аудио')
    is_main = models.BooleanField(default=False, verbose_name='На главном')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Музыка"
        verbose_name_plural = "Музыка"

class Concert(models.Model):
    name = models.CharField(max_length=200, verbose_name='Заголовок', blank=True)
    photo = models.ImageField(upload_to='concert_photos/', blank=True, verbose_name='Фото')
    location = models.CharField(max_length=200, verbose_name='Место', default='')
    date = models.DateTimeField(verbose_name='Дата', default=datetime.now)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость', default=0)
    description = models.TextField(verbose_name='Описание', blank=True)
    is_main = models.BooleanField(default=False, verbose_name='На главном')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Концерты"
        verbose_name_plural = "Концерты"


class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='news_photos/', null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
