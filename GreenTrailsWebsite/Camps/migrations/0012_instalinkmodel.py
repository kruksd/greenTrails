# Generated by Django 3.2.6 on 2021-10-16 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Camps', '0011_auto_20211016_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='instaLinkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insta_link1', models.CharField(max_length=2000)),
                ('insta_link2', models.CharField(max_length=2000)),
                ('insta_link3', models.CharField(max_length=2000)),
            ],
        ),
    ]
