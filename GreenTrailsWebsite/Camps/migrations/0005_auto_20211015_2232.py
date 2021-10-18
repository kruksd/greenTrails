# Generated by Django 3.2.6 on 2021-10-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Camps', '0004_alter_campmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campmodel',
            name='camp_brochure',
            field=models.FileField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='campmodel',
            name='image',
            field=models.ImageField(default='user-default.png', upload_to='images'),
        ),
    ]