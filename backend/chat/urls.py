from django.urls import path
from .views import all_chats, create_chat


urlpatterns = [
	# path('', views.show_all_chats, name='chat'),
	# path('<int:room_id>/', views.room_detail, name='room_detail'),
	path('api/create_chat', create_chat, name='create_chat'),
	path('api/all_chats', all_chats, name='all_chats'),
]
