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
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='concert_photos/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.title

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
