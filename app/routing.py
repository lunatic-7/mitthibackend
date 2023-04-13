from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path("ws/awsc/", ChatConsumer.as_asgi()),
]