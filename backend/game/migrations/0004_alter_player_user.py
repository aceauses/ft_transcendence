# Generated by Django 5.1.2 on 2024-12-16 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_rename_name_player_user'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]