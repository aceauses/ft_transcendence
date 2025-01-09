import logging
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from users.models import Profile
from .models import Game, Dashboard, Player
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Tournament

from django.middleware.csrf import get_token
import sys

# show recent games for now
@login_required
def recent_games(request):
	csrf_token_view(request)
	this_user = request.user
	if request.method == "POST":
		if 'opp_name' in request.POST:
			opponent = request.POST.get('opp_name', '').strip()
			if opponent:
				if User.objects.filter(username=opponent).exists():
					opp = User.objects.get(username=opponent)
					if opp != this_user:
						user_profile = Profile.objects.get(user=this_user)
						opp_profile = Profile.objects.get(user=opp)
						game = Game.objects.create(player1=user_profile, player2=opp_profile)
						game.save()
						return redirect('game:new_game', game_id=game.id)
					else:
						logging.error("You cannot play against yourself.")
						return render(request, "game/recent_games.html", {"error_message": "You cannot play against yourself."})
				else:
					logging.error("Invalid Username")
					return render(request, "game/recent_games.html", {"error_message": "Invalid opponent username."})
			else:
				logging.error("No Input")
				return render(request, "game/recent_games.html", {"error_message": "Please enter an opponent username."})
		if 'player2_enter_game' in request.POST:
			game_id = request.POST.get('player2_enter_game')
			return redirect('game:new_game', game_id=game_id)

	last_games = Game.objects.order_by("-played_at")[:10]
	return render(request, "game/base.html", {"recent_games_list": last_games })


def start_game(request, game_id):
	game = get_object_or_404(Game, id=game_id)
	return render(request, "game/start_game.html", {"game": game, "game_id": game_id})

def game_details(request, game_id):
	game = get_object_or_404(Game, pk=game_id)
	return render(request, "game/game_details.html", {"game": game})

def players(request):
	return render(request, "game/players.html", {"players_list": Player.objects.order_by("-created_at")[:10]})

def player_details_by_id(request, player_id):
	player = get_object_or_404(Player, pk=player_id)
	return render(request, "game/player_details.html", {"player": player})

def dashboard(request):
	return render(request, "game/dashboard.html", {"dashboard": Dashboard.get_instance()})

def csrf_token_view(request):
	csrf_token = get_token(request)
	print("Token:")
	print(csrf_token)
	sys.stdout.flush()



#tournaments functions 
def create_tournament(request):
	if request.method == "POST":
		tournament_name = request.POST.get("tournament_name")
		number_of_players = request.POST.get("number_of_players")

		# Validar los datos
		if not tournament_name or not number_of_players:
			return render(request, "game/tournament.html", {
				"error_message": "All fields are required.",
			})

		# Crear el torneo
		tournament = Tournament.objects.create(
			name=tournament_name,
			number_of_players=number_of_players,
			created_by=request.user,
			pending=True
		)
		tournament.players.add(request.user)
		tournament.save()

		# Redirigir a la página principal o mostrar un mensaje de éxito
		return redirect("game:tournament_list")  # Cambia esto según tu flujo

	return render(request, "game/tournament.html")

def tournament_list(request):
	tournaments = Tournament.objects.all()
	return render(request, "game/tournament_list.html", {"tournaments": tournaments})

def game_view(request):
    recent_games_list = Game.objects.filter(pending=False).order_by('-date')[:10]
    pending_games_list = Game.objects.filter(pending=True)
    recent_tournaments_list = Tournament.objects.filter(pending=False).order_by('-date')[:10]
    pending_tournaments_list = Tournament.objects.filter(pending=True)
    print("hello")  # Imprime la lista de torneos recientes después de recuperarla

    return render(request, "game/game_page.html", {
        "recent_games_list": recent_games_list,
        "pending_games_list": pending_games_list,
        "recent_tournaments_list": recent_tournaments_list,
        "pending_tournaments_list": pending_tournaments_list,
    })


def join_tournament(request, tournament_id):
	if request.method == "POST":
		tournament = Tournament.objects.get(id=tournament_id)
		if tournament.players.count() < tournament.number_of_players:
			tournament.players.add(request.user)
			tournament.save()
			# Redirigir a la página principal o mostrar un mensaje de éxito
			return redirect("game:tournament_list")  # Cambia esto según tu flujo
		else:
			return render(request, "game/tournament.html", {
				"error_message": "The tournament is full.",
			})
	return render(request, "game/tournament.html")