# Generated by Django 5.1.2 on 2024-11-18 17:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pong', '0001_squashed_0002_rename_pub_date_game_played_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='started_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date started'),
            preserve_default=False,
        ),
    ]
