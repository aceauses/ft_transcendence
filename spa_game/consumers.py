import json
import sys
from channels.generic.websocket import AsyncWebsocketConsumer

class BasePageConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		sys.stdout.flush()
		await self.accept()
		await self.send(text_data=json.dumps({
			"message": "Willkommen bei der Base Page WebSocket-Verbindung!"
		}))

	async def disconnect(self, close_code):
		print("WebSocket-Verbindung getrennt.")

	async def receive(self, text_data):
		data = json.loads(text_data)
		print(f"Nachricht empfangen: {data}")

		await self.send(text_data=json.dumps({
			"response": f"Nachricht empfangen: {data['message']}"
		}))
