# Generated by Django 4.1.7 on 2023-04-04 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_song_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='alboms',
            new_name='albums',
        ),
    ]
