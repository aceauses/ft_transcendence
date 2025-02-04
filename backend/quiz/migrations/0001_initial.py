# Generated by Django 5.1.5 on 2025-02-02 13:39

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
	initial = True

	dependencies = [
		migrations.swappable_dependency(settings.AUTH_USER_MODEL),
	]

	operations = [
		migrations.CreateModel(
			name='Participant',
			fields=[
				(
					'id',
					models.BigAutoField(
						auto_created=True,
						primary_key=True,
						serialize=False,
						verbose_name='ID',
					),
				),
				('joined_at', models.DateTimeField(auto_now_add=True)),
				('score', models.IntegerField(default=0)),
				('score_difference', models.IntegerField(default=0)),
				(
					'user',
					models.ForeignKey(
						on_delete=django.db.models.deletion.CASCADE,
						to=settings.AUTH_USER_MODEL,
					),
				),
			],
		),
		migrations.CreateModel(
			name='Room',
			fields=[
				('id', models.BigAutoField(primary_key=True, serialize=False)),
				('name', models.CharField(max_length=100, unique=True)),
				('created_at', models.DateTimeField(auto_now_add=True)),
				(
					'last_activity',
					models.DateTimeField(default=django.utils.timezone.now),
				),
				('is_active', models.BooleanField(default=True)),
				('game_started', models.BooleanField(default=False)),
				('current_question', models.JSONField(blank=True, null=True)),
				('shuffled_answers', models.JSONField(blank=True, null=True)),
				('questions', models.JSONField(blank=True, null=True)),
				('is_ingame', models.BooleanField(default=False)),
				('question_start', models.DateTimeField(blank=True, null=True)),
				(
					'leader',
					models.OneToOneField(
						blank=True,
						null=True,
						on_delete=django.db.models.deletion.SET_NULL,
						related_name='leader_of',
						to='quiz.participant',
					),
				),
			],
		),
		migrations.AddField(
			model_name='participant',
			name='room',
			field=models.ForeignKey(
				on_delete=django.db.models.deletion.CASCADE,
				related_name='participants',
				to='quiz.room',
			),
		),
		migrations.CreateModel(
			name='Answer',
			fields=[
				(
					'id',
					models.BigAutoField(
						auto_created=True,
						primary_key=True,
						serialize=False,
						verbose_name='ID',
					),
				),
				('answer_given', models.JSONField(blank=True, default=dict, null=True)),
				('question', models.JSONField(blank=True, default=dict, null=True)),
				('answered_at', models.DateTimeField(auto_now_add=True)),
				('is_disqualified', models.BooleanField(default=False)),
				(
					'participant',
					models.ForeignKey(
						on_delete=django.db.models.deletion.CASCADE,
						related_name='answers',
						to='quiz.participant',
					),
				),
				(
					'room',
					models.ForeignKey(
						on_delete=django.db.models.deletion.CASCADE,
						related_name='answers',
						to='quiz.room',
					),
				),
			],
		),
		migrations.CreateModel(
			name='RoomSettings',
			fields=[
				(
					'id',
					models.BigAutoField(
						auto_created=True,
						primary_key=True,
						serialize=False,
						verbose_name='ID',
					),
				),
				('question_count', models.PositiveSmallIntegerField(default=5)),
				('time_per_question', models.PositiveSmallIntegerField(default=30)),
				('difficulty', models.CharField(default='any', max_length=10)),
				('time_after_question', models.PositiveSmallIntegerField(default=20)),
				('time_after_game_end', models.PositiveSmallIntegerField(default=20)),
				('category', models.PositiveSmallIntegerField(default=0)),
				(
					'room',
					models.OneToOneField(
						on_delete=django.db.models.deletion.CASCADE,
						related_name='room_settings',
						to='quiz.room',
					),
				),
			],
		),
		migrations.AddField(
			model_name='room',
			name='settings',
			field=models.OneToOneField(
				blank=True,
				null=True,
				on_delete=django.db.models.deletion.CASCADE,
				related_name='room_settings',
				to='quiz.roomsettings',
			),
		),
	]
