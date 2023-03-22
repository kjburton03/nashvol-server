from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nashvolapi.models import EventVolunteers

class EventVolunteerView(ViewSet):
    def retrieve(self, request, pk):
        event_volunteer = EventVolunteers.objects.get(pk=pk)
        serializer = EventVolunteerSerializer(event_volunteer)
        return Response(serializer.data)

    def list(self, request):
        event_volunteers = EventVolunteers.objects.all()
        serializer = EventVolunteerSerializer(event_volunteers, many=True)
        return Response(serializer.data)

class EventVolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventVolunteers
        fields = ('id', 'volunteer', 'event')
