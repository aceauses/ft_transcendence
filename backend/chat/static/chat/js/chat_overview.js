import { create_chat_api } from './create_chat_api.js';

export async function chat_overview() {
	const contentElement = document.getElementById('chat-app-content');

	try {
		const response = await fetch('/chat/api/all_chats');
		if (!response.ok) {
			throw new Error(`HTTP error! Status: ${response.status}`);
		}
		const data = await response.json();
		const chats = data.chats;

		contentElement.innerHTML = `
			<div>
				<h1>All Chats</h1>
				<ul>
					${chats.map(chat => `
						<li>${chat.name} ${chat.id}</li>
					`).join('')}
				</ul>
			</div>
			<form id="create-chat-form">
				<input id="chat-api" type="text" name="chat-name" placeholder="Enter a chat Name" />
				<button id="create-chat-button" type="submit">Create</button>
			</form>
		`;
		document.getElementById("create-chat-form").addEventListener("submit", function (event) {
			event.preventDefault();
			create_chat_api(event);

			// delete what was in input
			let input = document.getElementById("chat-api"); 
			input.value = "";
		});
	} catch (error) {
		console.error('Error fetching chats:', error);
		contentElement.innerHTML = `<p>Fehler beim Laden der Chats.</p>`;
	}
}
