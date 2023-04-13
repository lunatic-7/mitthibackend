from django.urls import path
from . import views

urlpatterns = [
    # other urls here
    path('ullumano/messages/', views.chat_messages, name='message-list'),
]
