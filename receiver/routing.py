from django.urls import path
from .consumers import EquityConsumer

websocket_urlpatterns = [
    path("ws/equity/", EquityConsumer.as_asgi()),
]