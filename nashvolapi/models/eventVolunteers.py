from django.db import models
from django.contrib.auth.models import User


class EventVolunteers(models.Model):
    volunteer = models.ForeignKey("Volunteer", on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)

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








