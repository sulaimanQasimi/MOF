from django.db import models
class Door(models.Model):

    name = models.CharField(max_length=100)
    material = models.CharField(max_length=50)
    is_open=models.BooleanField(default=False)
    building=models.ForeignKey('Building', on_delete=models.CASCADE, related_name='doors')
    def __str__(self):
        return self.name
