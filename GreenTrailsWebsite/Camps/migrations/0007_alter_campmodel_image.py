# Generated by Django 3.2.6 on 2021-10-15 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Camps', '0006_alter_campmodel_camp_brochure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campmodel',
            name='image',
            field=models.ImageField(default='user-default.png', upload_to=''),
        ),
    ]
