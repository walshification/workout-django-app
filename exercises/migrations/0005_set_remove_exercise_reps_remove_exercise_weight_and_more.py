# Generated by Django 4.0 on 2021-12-14 03:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("exercises", "0004_alter_routine_owner"),
    ]

    operations = [
        migrations.CreateModel(
            name="Set",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("exercise", models.CharField(max_length=200)),
                ("weight", models.IntegerField(default=0)),
                ("reps", models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name="exercise",
            name="reps",
        ),
        migrations.RemoveField(
            model_name="exercise",
            name="weight",
        ),
        migrations.RemoveField(
            model_name="routine",
            name="completed_at",
        ),
        migrations.RemoveField(
            model_name="routine",
            name="is_completed",
        ),
        migrations.CreateModel(
            name="Workout",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("completed_at", models.DateTimeField(blank=True, null=True)),
                ("is_completed", models.BooleanField(default=False)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="workouts",
                        to="auth.user",
                    ),
                ),
                (
                    "set",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sets",
                        to="exercises.set",
                    ),
                ),
            ],
        ),
    ]
