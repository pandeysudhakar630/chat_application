import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import Message
from datetime import datetime

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Get the user id from URL and establish the connection
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.room_group_name = f"chat_{self.user_id}"

        # Join the chat room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the chat room
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json['message']
        sender = self.scope['user']

        # Save the message to the database
        receiver = await self.get_receiver_user(self.user_id)
        message = Message.objects.create(
            sender=sender,
            receiver=receiver,
            content=message_content,
            timestamp=datetime.now()
        )

        # Send message to WebSocket
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message_content,
                'sender': sender.username
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))

    async def get_receiver_user(self, user_id):
        return await database_sync_to_async(User.objects.get)(id=user_id)
