# Generated by Django 4.1.7 on 2023-04-06 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_alter_news_description_alter_news_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Merchandise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('image', models.ImageField(upload_to='merchandise', verbose_name='Фотография')),
                ('size', models.CharField(max_length=20, verbose_name='Размер')),
                ('color', models.CharField(max_length=20, verbose_name='Цвет')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Мерч',
                'verbose_name_plural': 'Мерч',
            },
        ),
        migrations.CreateModel(
            name='MerchandiseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория товаров',
                'verbose_name_plural': 'Категории товаров',
            },
        ),
        migrations.CreateModel(
            name='TShirt',
            fields=[
                ('merchandise_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='webapp.merchandise')),
                ('type', models.CharField(max_length=20, verbose_name='Тип')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.merchandisecategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Футболка',
                'verbose_name_plural': 'Футболки',
            },
            bases=('webapp.merchandise',),
        ),
        migrations.CreateModel(
            name='Cap',
            fields=[
                ('brim_type', models.CharField(max_length=50, verbose_name='Размер')),
                ('size_cap', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='webapp.merchandise', verbose_name='Тип козырька')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.merchandisecategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Кепка',
                'verbose_name_plural': 'Кепки',
            },
            bases=('webapp.merchandise',),
        ),
    ]
