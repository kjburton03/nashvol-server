"""View module for handling requests about events"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nashvolapi.models import Event, Volunteer, EventType
from rest_framework.decorators import action

class EventView(ViewSet):
    """Nashol events view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single event
        Returns:
            Response -- JSON serialized event
        """
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Event.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all events
        Returns:
            Response -- JSON serialized list of events
        """
        events = Event.objects.all()
        # volunteer = Volunteer.objects.get(user=request.auth.user)

        # # Set the `joined` property on every event
        # for event in events:
        #     # Check to see if the gamer is in the attendees list on the event
        #     event.joined = volunteer in event.attendees.all()

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

# class OrganizerSerializer(serializers.ModelSerializer):
#     """JSON serializer for organizers
#     """
#     class Meta:
#         model = Volunteer
#         fields = ('full_name',)

# class VolunteerSerializer(serializers.ModelSerializer):
#     """JSON serializer for attendees
#     """
#     class Meta:
#         model = Volunteer
#         fields = ('full_name',)


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """

    class Meta:
        model = Event
        fields = ('id', 'organizer', 'name', 'details', 'date', 'location', 'eventType', 'eventVolunteers'  )
