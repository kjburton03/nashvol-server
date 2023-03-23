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
        volunteer = Volunteer.objects.get(user=request.auth.user)
        
        # # Set the `joined` property on every event
        for event in events:
        #     # Check to see if the gamer is in the attendees list on the event
            event.joined = volunteer in event.eventVolunteers.all()

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized game instance
        """
        organizer = Volunteer.objects.get(user=request.auth.user)
        eventType = EventType.objects.get(pk=request.data["eventType"])
        # type = GameType.objects.get(pk=request.data["type"])

        event = Event.objects.create(

            location=request.data["location"],
            date=request.data["date"],
            name=request.data["name"],
            details=request.data["details"],
            # attendees=request.data["attendees"],
            organizer=organizer,
            eventType=eventType
        )
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        organizer = Volunteer.objects.get(user=request.auth.user)
        eventType = EventType.objects.get(pk=request.data["eventType"])

        event = Event.objects.get(pk=pk)
        event.name = request.data["name"]
        event.location = request.data["location"]
        event.date = request.data["date"]
        event.details = request.data["details"]
        event.organizer=organizer
        event.eventType=eventType


        event.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


    def destroy(self, request, pk):
        """Handle DELETE requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['post'], detail=True)
    def signup(self, request, pk):
        """Post request for a user to sign up for an event"""
        volunteer = Volunteer.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.eventVolunteers.add(volunteer)
        return Response({'message': 'volunteer added'}, status=status.HTTP_201_CREATED)
    @action(methods=['delete'], detail=True)
    def leave(self, request, pk):
        """Delete request for a user to leave an event"""
        volunteer = Volunteer.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.eventVolunteers.remove(volunteer)
        return Response({'message': 'Gamer removed'}, status=status.HTTP_204_NO_CONTENT)
# class OrganizerSerializer(serializers.ModelSerializer):
#     """JSON serializer for organizers
#     """
#     class Meta:
#         model = Volunteer
#         fields = ('full_name',)

class VolunteerSerializer(serializers.ModelSerializer):
    """JSON serializer for attendees
    """
    class Meta:
        model = Volunteer
        fields = ('full_name',)



class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """

    class Meta:
        model = Event
        fields = ('id', 'organizer', 'name', 'details', 'date', 'location', 'eventType', 'eventVolunteers', 'joined'  )
