
/**
 * Sends a Post request to the server to submit an answer.
 */
export function submitAnswer(roomId, question, answer) {
	const csrfToken = document.querySelector('meta[name="csrf-token"]').content;
	fetch(`/quiz/submit_answer/${roomId}/`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': csrfToken
		},
		body: JSON.stringify({question: question, answer: answer })
	})
	.then(response => response.json())
	.then(data => {
		if (data.success) {
			console.log('Answer submitted successfully');
		} else {
			console.error('Error submitting answer:', data.error);
		}
	})
	.catch(error => {
		console.error('An error occurred:', error);
	});
}

/**
 * Displays the question and answer options.
 */
export function displayQuestion(question, answers) {
	const questionContainer = document.getElementById('question-container');
	const answerOptions = document.getElementById('answer-options');
	const quizQuestionContainer = document.getElementById('quiz-questions');

	questionContainer.innerHTML = question;
	answerOptions.innerHTML = '';

	answers.forEach((answer, index) => {
		const button = document.createElement('button');
		button.className = 'answer-option btn btn-primary';
		button.setAttribute('data-answer', answer);
		button.innerText = answer;
		button.addEventListener('click', function () {
			const answer = this.getAttribute('data-answer');
			const currentRoom = JSON.parse(localStorage.getItem('currentRoom'));
			submitAnswer(currentRoom.room_id, question, answer);
		});
		answerOptions.appendChild(button);
	});
	quizQuestionContainer.style.display = 'block';
}

/**
 * Displays the correct answer (colours the buttons).
 */
export function displayCorrectAnswer(correctAnswer) {
	const answerButtons = document.querySelectorAll('.answer-option');

	answerButtons.forEach(button => {
		button.disabled = true;
		const answer = button.getAttribute('data-answer');
		if (answer === correctAnswer) {
			button.style.backgroundColor = 'green';
		} else {
			button.style.backgroundColor = 'red';
		}
	});
}

/**
 * Clears the question and answer options.
 */
export function clearQuestionAndAnswers() {
	const questionContainer = document.getElementById('question-container');
	const answerOptions = document.getElementById('answer-options');
	const quizQuestionContainer = document.getElementById('quiz-questions');

	questionContainer.innerHTML = '';
	answerOptions.innerHTML = '';
	quizQuestionContainer.style.display = 'none';
}
