# Generated by Django 3.2.6 on 2021-10-15 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Camps', '0005_auto_20211015_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campmodel',
            name='camp_brochure',
            field=models.FileField(upload_to=''),
        ),
    ]
