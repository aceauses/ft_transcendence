import { CreateGameForm } from './CreateGame.js';

export function game_base() {
	const socket = new WebSocket("ws://localhost:8000/ws/game/");
	const userName = document.getElementById('username').getAttribute('data-username');

	// open socket
	socket.onopen = () => {
		console.log("WebSocket-Verbindung hergestellt.");
		socket.send(JSON.stringify({ message: "Hallo, Server!" }));
	};

	console.log("WebSocket-basierte Base Page");

	fetch('/game/api/game-data/')
		.then(response => response.json())
		.then(games => {
			console.log(games);
			const recentGames = games
				.filter(game => !game.pending)
				.map(game => `
					<a href="/game/${game.game_id}" class="ChatButtonBackground">
						${game.player1} vs ${game.player2} (${game.score1}-${game.score2})
					</a>
				`).join('');

			const pendingGames = games
				.filter(game => game.pending)
				.map(game => `
					<a href="/game/pong/${game.game_id}" class="ChatButtonBackground" data-link>
						${game.player1} vs ${game.player2} (pending)
					</a>
				`).join('');

			document.getElementById('pong-app-content').innerHTML = `
				<h2>Recent Games</h2>
				<div>${recentGames || '<p>No games have been played yet.</p>'}</div>

				<h2>Pending Games</h2>
				<div id="pendingGamesContainer">${pendingGames || '<p>No pending games.</p>'}</div>

				<h3>Play new Game</h3>
				<form id="create-game-form">
					<input id="opp_name" type="text" name="opp_name" placeholder="Enter opponent's Username" />
					<button class="add_user" type="submit">Play Game +</button>
				</form>
				<a href="/game/page2" data-link>page2</a>
				<a href="/game/pong/5" data-link>Game page</a>
			`;

			document.getElementById("create-game-form").addEventListener("submit", function(event) {
				event.preventDefault();
				CreateGameForm(event, socket);
			});
		})
		.catch(error => console.error("Fehler beim Laden der Daten:", error));

	// create Websocket
	// recv message from server
	socket.onmessage = (event) => {
		console.log("received data", event.data);
		const message = JSON.parse(event.data);
		if (message.message === "game_created") {
			console.log(message.game_id);
			console.log(message.player1);
			console.log(message.player2);
			if (userName == message.player1 || userName == message.player2)
			{
				const newGameHTML = `
					<a href="/game/pong/${message.game_id}" class="ChatButtonBackground" data-link>
						${message.player1} vs ${message.player2} (pending)
					</a>
				`;

				const pendingGamesContainer = document.getElementById('pendingGamesContainer');
				pendingGamesContainer.insertAdjacentHTML('afterbegin', newGameHTML);
			}
		}
	};

	socket.onclose = () => {
		console.log("WebSocket-Verbindung geschlossen.");
	};

	socket.onerror = (error) => {
		console.error("WebSocket-Fehler:", error);
	};
}