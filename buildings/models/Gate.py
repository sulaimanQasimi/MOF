from django.db import models
class Gate(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    is_main=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name