# Generated by Django 4.1.7 on 2023-04-07 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_news_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Цена'),
        ),
    ]
