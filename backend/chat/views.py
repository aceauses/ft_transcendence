# chat/views.py
import sys
import json
from django.http import JsonResponse
from .models import Group, Message, Chat

def all_chats(request):
	user = request.user
	chat_rooms = user.chat_groups.all().order_by('date_created')
	chat_list = [{"id": group.id, "name": group.groupName} for group in chat_rooms]
	return JsonResponse({"chats": chat_list})

def create_chat(request):
	if request.method == "POST":
		user = request.user
		if not user.is_authenticated:
			return JsonResponse({'error': 'User not authenticated'}, status=401)
		
		data = json.loads(request.body)
		chat_name = data.get('chat_name')

		if not chat_name:
			return JsonResponse({'error': 'Chat name is required'}, status=400)
		
		group = Group.objects.create(groupName=chat_name)
		group.members.add(user)
		
		return JsonResponse({'success': f'Chat {chat_name} created', 'group_id': group.id})
	return JsonResponse({'error': 'Invalid request method'}, status=405)


# def room_detail(request, room_id):
# 	user = request.user
# 	group = Group.objects.get(id=room_id)
# 	messages = group.messages.all().order_by('date_posted')
# 	members = group.members.all()

# 	# checks if the user is in the Group he trys to access
# 	is_in_group = False
# 	for member in members:
# 		if member == user:
# 			is_in_group = True
# 	if not is_in_group:
# 		return redirect('chat')

# 	# print(test.group.groupName)
# 	return render(
# 		request,
# 		'chat/ChatRoom.html',
# 		{'messages': messages, 'group': group, 'room_id': room_id, 'members': members},
# 	)