// router.js

export class SimpleRouter {
	constructor() {
		this.routes = {};
		this.init();
	}

	addRoute(path, handler) {
		this.routes[path] = handler;
	}

	navigateTo(path) {
		window.history.pushState({}, '', path);
		this.handleRouteChange();
	}

	handleRouteChange() {
		const path = window.location.pathname;
		const handler = this.routes[path];

		if (handler) {
			handler();
		} else {
			this.showNotFound();
		}
	}

	showNotFound() {
		document.getElementById('pong-app-content').innerHTML = '<h2>404 - Seite nicht gefunden</h2>';
	}

	init() {
		// Popstate-Ereignisse verarbeiten
		window.addEventListener('popstate', () => this.handleRouteChange());
		this.handleRouteChange();

		// Klicks auf Links abfangen
		document.body.addEventListener('click', (event) => {
			if (event.target.matches('[data-link]')) {
				event.preventDefault(); // Standard-Browser-Verhalten unterbinden
				const path = event.target.getAttribute('href'); // Link-Pfad abrufen
				this.navigateTo(path); // Router steuert die Navigation
			}
		});
	}
}
