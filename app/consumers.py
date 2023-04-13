import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Group, Chat


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # Join room group
        await self.channel_layer.group_add(
            'chat_room',
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            'chat_room',
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json

        # Find group object
        group = await database_sync_to_async(Group.objects.get)(name="chat_room")

        # Create new chat object
        chat = Chat(
            content=message["message"],
            group=group,
            senderId=message["senderId"],
            receiverId=message["receiverId"],
        )

        await database_sync_to_async(chat.save)()
        # Broadcast message to room group
        await self.channel_layer.group_send(
            'chat_room',
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        ev = event["message"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': ev["message"],
            'senderId': ev["senderId"],
            'receiverId': ev["receiverId"],
        }))
