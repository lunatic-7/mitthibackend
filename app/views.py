from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Chat
from .serializers import MessageSerializer

@api_view(['GET'])
def chat_messages(request):
    messages = Chat.objects.all().order_by('-timestamp') # Sort by timestamp
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)
