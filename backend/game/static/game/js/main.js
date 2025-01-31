// main.js

import { SimpleRouter } from './router.js';
import { page1, page2 } from './pages.js';
import { game } from './game.js';
import { gameDetails } from './gameDetails.js';
import { game_base } from './game_base_socket.js';

const router = new SimpleRouter();

router.addRoute('/game/pong/:game_id', (params) => {
	console.log("Game ID:", params.game_id);
	game(params);
	});

router.addRoute('/game/game-details/:game_id', (params) => {
	console.log("Game ID:", params.game_id);
	gameDetails(params);
	});

router.addRoute('/game/page1', page1);
router.addRoute('/game/page2', page2);
router.addRoute('/game', game_base);

router.navigateTo('/game');
