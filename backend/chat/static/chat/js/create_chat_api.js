

export function create_chat_api(event) {
	event.preventDefault();
	const chat_name = document.getElementById("chat-api").value.trim();

	if (!chat_name) {
		alert("Bitte einen Chatnamen eingeben!");
		return;
	}
	const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;


	fetch('/chat/api/create_chat', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': csrfToken,
		},
		body: JSON.stringify({ chat_name: chat_name }),
	})
	.then(response => response.json())
	.then(data => {
		if (data.success) {
			console.log("Chat erstellt:", data.success);
		} else {
			console.error("Fehler:", data.error);
		}
	})
	.catch(error => {
		console.error('Error:', error);
	});
}
