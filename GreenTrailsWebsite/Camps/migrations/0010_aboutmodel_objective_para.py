# Generated by Django 3.2.6 on 2021-10-15 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Camps', '0009_aboutmodel_about_latest'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='objective_para',
            field=models.CharField(default='para', max_length=5000),
            preserve_default=False,
        ),
    ]