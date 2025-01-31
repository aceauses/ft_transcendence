// main.js

import { SimpleRouter } from './router.js';
import { page1, page2 } from './pages.js';
import { game_base } from './game_base_socket.js';

const router = new SimpleRouter();

router.addRoute('/spa_game/page1', page1);
router.addRoute('/spa_game/page2', page2);
router.addRoute('/spa_game/', game_base);

router.navigateTo('/spa_game/');
