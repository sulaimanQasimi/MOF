from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    department_code = models.CharField(max_length=10, unique=True,editable=False)
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        ordering = ['name']
    def __str__(self):
        return self.name