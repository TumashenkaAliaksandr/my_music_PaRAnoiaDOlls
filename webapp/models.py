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
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    location = models.CharField(max_length=200, verbose_name='Место', default='')
    photo = models.ImageField(upload_to='news_photos/', null=True, blank=True, verbose_name='Фото')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"


class Merchandise(models.Model):
    # Название товара (строка до 100 символов)
    name = models.CharField(max_length=100, verbose_name='Название')
    # Описание товара (текстовое поле)
    description = models.TextField(verbose_name='Описание')
    # Цена товара (десятичное число с точностью до 2 знаков после запятой)
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена')
    # Изображение товара (загружаемое изображение, сохраняемое в папке 'merchandise')
    image = models.ImageField(upload_to='merchandise', verbose_name='Фотография')
    # Размер товара (строка до 20 символов)
    size = models.CharField(max_length=20, verbose_name='Размер')
    # Цвет товара (строка до 20 символов)
    color = models.CharField(max_length=20, verbose_name='Цвет')
    # Количество товара в наличии (целое число)
    quantity = models.IntegerField(verbose_name='Количество')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мерч"
        verbose_name_plural = "Мерч"


class MerchandiseCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'


class TShirt(Merchandise):
    category = models.ForeignKey(MerchandiseCategory, on_delete=models.CASCADE, verbose_name='Категория')
    type = models.CharField(max_length=20, verbose_name='Тип')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Футболка"
        verbose_name_plural = "Футболки"


class Cap(Merchandise):
    category = models.ForeignKey(MerchandiseCategory, on_delete=models.CASCADE, verbose_name='Категория')
    brim_type = models.CharField(max_length=50, verbose_name='Размер')
    size_cap = models.OneToOneField(Merchandise, parent_link=True, on_delete=models.CASCADE, verbose_name='Тип козырька')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кепка"
        verbose_name_plural = "Кепки"


class Sweatshirt(Merchandise):
    category = models.ForeignKey(MerchandiseCategory, on_delete=models.CASCADE, verbose_name='Категория')
    type = models.CharField(max_length=20, verbose_name='Тип')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Байка"
        verbose_name_plural = "Байка"

class Trinkets(Merchandise):
    category = models.ForeignKey(MerchandiseCategory, on_delete=models.CASCADE, verbose_name='Категория')
    type = models.CharField(max_length=20, verbose_name='Тип')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Разное"
        verbose_name_plural = "Разное"