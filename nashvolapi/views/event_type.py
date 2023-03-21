"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nashvolapi.models import EventType

class EventTypeView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        event_type = EventType.objects.get(pk=pk)
        serializer = EventTypeSerializer(event_type)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        event_types = EventType.objects.all()
        serializer = EventTypeSerializer(event_types, many=True)
        return Response(serializer.data)
class EventTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = EventType
        fields = ('id', 'eventType')
