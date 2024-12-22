# Generated by Django 5.1.2 on 2024-12-19 19:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_game_player1_control_settings_and_more'),
        ('users', '0002_profile_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='player1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_as_player1', to='users.profile'),
        ),
        migrations.AlterField(
            model_name='game',
            name='player2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_as_player2', to='users.profile'),
        ),
    ]