

export function game_base() {
	console.log("WebSocket-basierte Base Page");

	const app = document.getElementById('pong-app-content');
	app.innerHTML = `
		<h1>Willkommen auf der Base Page (WebSocket)</h1>
		<p>Warten auf Nachrichten vom Server...</p>
		<div id="ws-content"></div>
		<a href="/spa_game/page1" data-link>Gehe zu Seite 1</a>
		<a href="/spa_game/page2" data-link>Gehe zu Seite 2</a>
	`;

	// create Websocket
	const socket = new WebSocket("ws://localhost:8000/ws/spa_game/");


	// open socket
	socket.onopen = () => {
		console.log("WebSocket-Verbindung hergestellt.");
		socket.send(JSON.stringify({ message: "Hallo, Server!" }));
	};

	// recv message from server
	socket.onmessage = (event) => {
		console.log("Nachricht erhalten:", event.data);
		const wsContent = document.getElementById('ws-content');
		wsContent.innerHTML = `<p>${event.data}</p>`;
	};

	socket.onclose = () => {
		console.log("WebSocket-Verbindung geschlossen.");
		app.innerHTML += `<p style="color: red;">Verbindung zum Server verloren.</p>`;
	};

	socket.onerror = (error) => {
		console.error("WebSocket-Fehler:", error);
	};
}
