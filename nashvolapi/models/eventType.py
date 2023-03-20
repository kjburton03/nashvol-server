from django.db import models

class EventType(models.Model):

    eventType = models.CharField(max_length=59)