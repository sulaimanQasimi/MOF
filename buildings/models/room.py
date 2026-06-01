from django.db import models

from hr.models import Department

from .building import Building


class Room(models.Model):
    Room_Status = [
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('maintenance', 'Maintenance'),
        ('reserved', 'Reserved'),
    ]
    status = models.CharField(max_length=50, choices=Room_Status, default='available')
    floor = models.IntegerField()
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='rooms',null=True,blank=True)
    def __str__(self):
        return self.room_number
