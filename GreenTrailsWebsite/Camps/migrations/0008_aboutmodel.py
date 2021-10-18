# Generated by Django 3.2.6 on 2021-10-15 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Camps', '0007_alter_campmodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_para', models.CharField(max_length=5000)),
                ('about_image', models.ImageField(default='20210706_170841-01.jpeg', upload_to='')),
                ('mission_para', models.CharField(max_length=5000)),
                ('vision_para', models.CharField(max_length=5000)),
            ],
        ),
    ]