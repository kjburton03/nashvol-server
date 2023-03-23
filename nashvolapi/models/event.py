from django.db import models
from django.contrib.auth.models import User
class Event(models.Model):

    organizer = models.ForeignKey('Volunteer', on_delete=models.CASCADE, related_name='events_created_by_user')
    name = models.CharField(max_length=33)
    details = models.CharField(max_length=300)
    date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=200)
    eventType = models.ForeignKey('EventType', null=False, on_delete=models.CASCADE)

    eventVolunteers = models.ManyToManyField('Volunteer', through='EventVolunteers')

    @property
    def joined(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__joined
    @joined.setter
    def joined(self, value):
        self.__joined = value

    @property
    def organizerOfEvent(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__organizerOfEvent
    @organizerOfEvent.setter
    def organizerOfEvent(self, value):
        self.__organizerOfEvent = value
