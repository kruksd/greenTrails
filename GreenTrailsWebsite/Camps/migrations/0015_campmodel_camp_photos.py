# Generated by Django 3.2.6 on 2021-10-18 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Camps', '0014_youtubemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='campmodel',
            name='camp_photos',
            field=models.TextField(default='null', max_length=2000),
            preserve_default=False,
        ),
    ]
