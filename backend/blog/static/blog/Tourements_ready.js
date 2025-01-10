document.addEventListener("DOMContentLoaded", function () {
	document.querySelector("#pair_one").onclick = async function () {
	  console.log("Button clicked!");
  
	//   const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  
	  try {
		const response = await fetch('/game/api/create-game/', {
		  method: 'POST',
		  headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': csrfToken,
		  },
		  body: JSON.stringify({
			opponent: "Jsanger",
			username: "NewUser",
		  }),
		});
  
		const data = await response.json(); // Await the response to get the actual data
  
		if (response.ok) {
		  window.location.href = '/game/new/' + data.game_id + '/';
		} else {
		  console.error('Request failed with status:', response.status);
		  console.error('Error message:', data); // Displaying error message from response body
		}
	  } catch (error) {
		console.error('Fetch error:', error);
	  }
	};
  });
  