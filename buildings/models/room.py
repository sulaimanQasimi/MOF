from django.db import models

from .building import Building


class Room(models.Model):
    room_number = models.CharField(max_length=10)
    floor = models.IntegerField()
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='rooms')
