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
						print("HelloWorld")
						sys.stdout.flush()
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
	last_tournements = Tournament.objects.order_by("-created_at")[:10]
	return render(request, "game/base.html", {"recent_games_list": last_games, "recent_tournement_list": last_tournements })


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
		player_created = Player.objects.get(id=request.user.id)
		print(player_created)
		sys.stdout.flush()
		tournament.players.add(player_created)
		tournament.save()

		# Redirigir a la página principal o mostrar un mensaje de éxito
		return redirect("game:tournament_list")  # Cambia esto según tu flujo

	return render(request, "game/tournament.html")

def tournament_list(request):
	tournaments = Tournament.objects.all()
	any_pending = any(tournament.pending for tournament in tournaments)
	return render(request, "game/tournament_list.html", {"tournaments": tournaments, "any_pending": any_pending})

def game_view(request):
	# recent_games_list = Game.objects.filter(pending=False).order_by('-date')[:10]
	# pending_games_list = Game.objects.filter(pending=True)
	recent_tournaments_list = Tournament.objects.filter(pending=False).order_by('-date')[:10]
	pending_tournaments_list = Tournament.objects.filter(pending=True)
	tournaments = Tournament.objects.all()
	print("hello")  # Imprime la lista de torneos recientes después de recuperarla

	return render(request, "game/base.html", {
		"recent_games_list": recent_games_list,
		"pending_games_list": pending_games_list,
		"recent_tournaments_list": recent_tournaments_list,
		"pending_tournaments_list": pending_tournaments_list,
		"tournaments": tournaments, 
	})


def join_tournament(request, tournament_id):
	if request.method == "POST":
		tournament = Tournament.objects.get(id=tournament_id)
		if tournament.players.count() < tournament.number_of_players:
			test_player = Player.objects.get(id=request.user.id)
			tournament.players.add(test_player)
			tournament.save()
			# Redirect to the tournament details page
			return redirect("game:tournament_details", tournament_id=tournament_id)
		else:
			return render(request, "game/tournament.html", {
				"error_message": "The tournament is full.",
			})
	return render(request, "game/tournament.html")

def tournament_details(request, tournament_id):
	tournament = Tournament.objects.get(id=tournament_id)
	players = list(tournament.players.all())  # Obtén la lista de jugadores

	wons1 = 0
	wons2 = 0
	wons3 = 0
	wons4 = 0

	# Jugador 1
	if len(players) > 0:
		if 'wons1' not in request.session:
			# Guardamos SOLO el número de victorias, no el objeto
			request.session['wons1'] = players[0].matches_won
		wons1 = request.session['wons1']

	# Jugador 2
	if len(players) > 1:
		if 'wons2' not in request.session:
			# De nuevo, guardamos solo matches_won del jugador 2
			request.session['wons2'] = players[1].matches_won
		wons2 = request.session['wons2']

	# Jugador 3
	if len(players) > 2:
		if 'wons3' not in request.session:
			request.session['wons3'] = players[2].matches_won
		wons3 = request.session['wons3']

	# Jugador 4
	if len(players) > 3:
		if 'wons4' not in request.session:
			request.session['wons4'] = players[3].matches_won
		wons4 = request.session['wons4']

	# Organiza los jugadores en pares (si lo necesitas)
	player_pairs = []
	for i in range(0, len(players), 2):
		pair = (players[i], players[i + 1] if i + 1 < len(players) else None)
		player_pairs.append(pair)
	
	player0_ready = False
	if request.method == "POST":
		if "player0_button_clicked" in request.POST:
			player0_ready = True
			# Aquí cualquier lógica adicional

	return render(request, "game/tournament_details.html", {
		"tournament": tournament,
		"players": players,
		"player0_ready": player0_ready,
		"wons1": wons1,
		"wons2": wons2,
		"wons3": wons3,
		"wons4": wons4,
	})
# game = Game.objects.get(id=game_id)
# if (game.played_at != game.started_at)
# 	game Done
# 	if (game.score1 > game.score2)
# 		player1 Winner
# 	else
# 		player2 = winner