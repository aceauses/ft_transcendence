# Generated by Django 5.1.2 on 2024-12-22 18:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('games_played', models.IntegerField(default=0)),
                ('active_players', models.IntegerField(default=0)),
                ('leaderboard', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_for_player', to='users.profile')),
                ('created_at', models.DateTimeField(verbose_name='date created')),
                ('matches_won', models.IntegerField(default=0)),
                ('matches_lost', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score1', models.IntegerField(default=0)),
                ('score2', models.IntegerField(default=0)),
                ('started_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('played_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_as_player1', to='game.player')),
                ('player1_control_settings', models.CharField(default='up down', max_length=255)),
                ('player1_ready', models.BooleanField(default=False)),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_as_player2', to='game.player')),
                ('player2_control_settings', models.CharField(default='up down', max_length=255)),
                ('player2_ready', models.BooleanField(default=False)),
                ('pending', models.BooleanField(default=True)),
            ],
        ),
    ]
