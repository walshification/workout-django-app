# Generated by Django 4.0 on 2021-12-15 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0007_remove_workout_exercise_routine_workout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routine',
            name='workout',
        ),
        migrations.AddField(
            model_name='workout',
            name='routine',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='exercises.routine'),
            preserve_default=False,
        ),
    ]