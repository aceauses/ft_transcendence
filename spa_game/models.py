from django.db import models

class Game(models.Model):
	game_name = models.CharField(max_length=100, default="game")
	is_active = models.BooleanField(default=True)  # Ein einfaches Bool-Feld
	
	def __str__(self):
		return f"Game active: {self.is_active}"
