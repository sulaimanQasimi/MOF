from django.db import models
import Gate
class Building(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200)
    height = models.FloatField()
    year_built = models.IntegerField()
    gate=models.ForeignKey(Gate, on_delete=models.CASCADE, related_name='buildings')


    def __str__(self):
        return self.name