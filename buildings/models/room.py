from django.db import models
from django.db.models import CheckConstraint
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
    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'
        ordering = ['room_number']
        constraints = [
            models.CheckConstraint(check=models.Q(floor__gte=0), name="floor_gte_0"),
            models.CheckConstraint(check=models.Q(room_number__length=10), name="room_number_length_10"),
            models.CheckConstraint(check=models.Q(room_number__unique=True), name="room_number_unique"),
            models.CheckConstraint(check=models.Q(room_number__max_length=10), name="room_number_max_length_10"),
            models.CheckConstraint(check=models.Q(room_number__min_length=10), name="room_number_min_length_10"),
        ]
        indexes = [
            models.Index(fields=['room_number', 'floor', 'building', 'department']),
        ]
    def __str__(self):
        return self.room_number
