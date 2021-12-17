# Generated by Django 4.0 on 2021-12-15 00:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exercises", "0009_remove_exercise_routine_remove_exercise_set_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="exercise",
            name="routine",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="exercises.routine",
            ),
            preserve_default=False,
        ),
    ]
