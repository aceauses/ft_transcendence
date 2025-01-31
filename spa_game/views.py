from django.shortcuts import render
from django.http import JsonResponse
from .models import Game
import sys

def game_home(request):
	return render(request, 'spa_game/index.html')

def page_data(request):
	try:
		games = Game.objects.all()
		data = []
		
		for game in games:
			game_data = {
				'game': game.game_name,
				'active': game.is_active,
				'id': game.id,
			}
			data.append(game_data)
		
		return JsonResponse(data, safe=False)
		
	except Game.DoesNotExist:
		return JsonResponse({'error': 'Keine Spiele gefunden'}, status=404)
