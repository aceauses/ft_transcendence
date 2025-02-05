from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    re_path(r'new/(?P<game_id>\d+)/$', consumers.GameConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/tournament/", consumers.TournamentConsumer.as_asgi()),
    ]),
})