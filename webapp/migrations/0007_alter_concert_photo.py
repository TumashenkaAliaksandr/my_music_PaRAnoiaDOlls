# Generated by Django 4.1.7 on 2023-04-04 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_concert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='photo',
            field=models.ImageField(upload_to='concert_photos/'),
        ),
    ]
