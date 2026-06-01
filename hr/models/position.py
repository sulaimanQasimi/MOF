from django.db import models
from .department import Department
class Position(models.Model):
    Position_Type = [
        ('manager', 'Manager'),
        ('employee', 'Employee'),
        ('intern', 'Intern'),
    ]
    name = models.CharField(max_length=100)
    position_code = models.CharField(max_length=10, unique=True,editable=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=Position_Type)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    vacancy = models.IntegerField()
    def __str__(self):
        return self.name