# Generated by Django 5.1.5 on 2025-02-02 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
	initial = True

	dependencies = [
		('game', '0001_initial'),
		('users', '0001_initial'),
	]

	operations = [
		migrations.AddField(
			model_name='player',
			name='profile',
			field=models.OneToOneField(
				on_delete=django.db.models.deletion.CASCADE,
				related_name='profile_for_player',
				to='users.profile',
			),
		),
		migrations.AddField(
			model_name='game',
			name='player1',
			field=models.ForeignKey(
				on_delete=django.db.models.deletion.CASCADE,
				related_name='games_as_player1',
				to='game.player',
			),
		),
		migrations.AddField(
			model_name='game',
			name='player2',
			field=models.ForeignKey(
				on_delete=django.db.models.deletion.CASCADE,
				related_name='games_as_player2',
				to='game.player',
			),
		),
	]
