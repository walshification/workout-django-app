# Generated by Django 4.0 on 2021-12-13 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routine',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
