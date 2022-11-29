from django.urls import re_path,path

from DataManager.consumers import DataSocket
print("root")
websocket_urlpatterns = [
    # path('ws/chat/<str:room_id>', ChatConsumer.as_asgi()),
    re_path(r'ws/data/', DataSocket.as_asgi(),name='data_chanel'),
    # re_path(r'wss/chat/(?P<room_id>[0-9a-f-]+)/$', ChatConsumer.as_asgi(),name='chat'),
]