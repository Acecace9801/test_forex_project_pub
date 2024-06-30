import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class EquityConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.user = None

    def connect(self):
        self.user = self.scope['user']
        if self.user.is_authenticated:
            async_to_sync(self.channel_layer.group_add)(
                self.user.username,
                self.channel_name
            )
            self.accept()
        self.close()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.user.username,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

    # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.user.username, {"type": "chat.message", "message": message}
        )

    def chat_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps({"message": message}))