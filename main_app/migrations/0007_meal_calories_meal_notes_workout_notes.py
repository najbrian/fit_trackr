# Generated by Django 4.2.16 on 2024-09-19 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_workout_reps_workout_sets'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='calories',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
