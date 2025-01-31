
export class SimpleRouter {
	constructor() {
		this.routes = [];
		this.init();
	}

	addRoute(path, handler) {
		const paramNames = [];
		const regexPath = path.replace(/\/:([\w]+)/g, (_, paramName) => {
			paramNames.push(paramName);
			return "/([^/]+)";
		});

		this.routes.push({ regex: new RegExp(`^${regexPath}$`), handler, paramNames });
	}

	navigateTo(path) {
		window.history.pushState({}, '', path);
		this.handleRouteChange();
	}

	handleRouteChange() {
		const path = window.location.pathname;
		
		for (const route of this.routes) {
			const match = path.match(route.regex);
			if (match) {
				const params = {};
				route.paramNames.forEach((name, index) => {
					params[name] = match[index + 1]; // Parameter zuordnen
				});

				route.handler(params);
				return;
			}
		}

		this.showNotFound();
	}

	showNotFound() {
		document.getElementById('pong-app-content').innerHTML = '<h2>404 - Seite nicht gefunden</h2>';
	}

	init() {
		window.addEventListener('popstate', () => this.handleRouteChange());
		this.handleRouteChange();

		document.body.addEventListener('click', (event) => {
			if (event.target.matches('[data-link]')) {
				event.preventDefault();
				const path = event.target.getAttribute('href');
				this.navigateTo(path);
			}
		});
	}
}

