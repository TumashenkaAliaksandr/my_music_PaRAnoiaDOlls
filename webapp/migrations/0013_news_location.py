# Generated by Django 4.1.7 on 2023-04-07 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_merchandise_merchandisecategory_tshirt_cap'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='location',
            field=models.CharField(default='', max_length=200, verbose_name='Место'),
        ),
    ]
