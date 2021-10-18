# Generated by Django 3.2.6 on 2021-10-16 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Camps', '0010_aboutmodel_objective_para'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campmodel',
            old_name='activities',
            new_name='camp_activities',
        ),
        migrations.RenameField(
            model_name='campmodel',
            old_name='carried_things',
            new_name='camp_carried_things',
        ),
        migrations.RenameField(
            model_name='campmodel',
            old_name='exclusions',
            new_name='camp_exclusions',
        ),
        migrations.RenameField(
            model_name='campmodel',
            old_name='guidelines',
            new_name='camp_guidelines',
        ),
        migrations.RenameField(
            model_name='campmodel',
            old_name='inclusions',
            new_name='camp_inclusions',
        ),
        migrations.RenameField(
            model_name='campmodel',
            old_name='instructions',
            new_name='camp_instructions',
        ),
        migrations.RenameField(
            model_name='campmodel',
            old_name='packages',
            new_name='camp_packages',
        ),
        migrations.RenameField(
            model_name='campmodel',
            old_name='places_to_visit',
            new_name='camp_places_to_visit',
        ),
        migrations.RenameField(
            model_name='campmodel',
            old_name='suggestions',
            new_name='camp_suggestions',
        ),
    ]