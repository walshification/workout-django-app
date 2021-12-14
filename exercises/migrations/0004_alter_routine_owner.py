# Generated by Django 4.0 on 2021-12-13 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('exercises', '0003_remove_exercise_routine_exercise_routine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routine',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routines', to='auth.user'),
        ),
    ]