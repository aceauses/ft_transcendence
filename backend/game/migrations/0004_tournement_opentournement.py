# Generated by Django 5.1.5 on 2025-02-05 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_tournement'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournement',
            name='openTournement',
            field=models.BooleanField(default=True),
        ),
    ]
