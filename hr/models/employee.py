from django.db import models
from .position import Position
from .department import Department
class Employee(models.Model):
    Gender = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=Gender)
    birth_date = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    hire_date = models.DateField()
    leave_date = models.DateField()
    is_active = models.BooleanField(default=True)
    
    @property
    def full_name(self):
        return f"{self.name} {self.surname}"