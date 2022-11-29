import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import async_to_sync
from channels.db import database_sync_to_async

from django.db.models import Q


class DataSocket(AsyncWebsocketConsumer):
    async def connect(self):
        print("connetin")
        self.room_id = self.scope['url_route']['kwargs']

        print(self.room_id)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.channel_name
        )
    # @AsyncWebsocketConsumer
    # @database_sync_to_async
    # def get_user(self,id):
    #     try:
    #         return CustomUserModel.objects.get(id=id)
    #     except:
    #         return False

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.scope['user']
        print(message)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'sender': {
                    'id':user.id,
                    'username':user.username
                },
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'sender':{
                    'id':sender.get('id'),
                    'username':sender.get('username')
                },
            'message': message
        }))
