from django.db import models
from django.contrib.auth.models import User


class EventVolunteers(models.Model):
    volunteer = models.ForeignKey("Volunteer", on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)