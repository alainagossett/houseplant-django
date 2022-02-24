from django.db import models
from datetime import date

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=280)
    sunlight = models.CharField(max_length=100)
    water = models.CharField(max_length=100)
    issues = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Watering(models.Model):
    date = models.DateField('watering_date')
    rotated = models.BooleanField(default=False)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"Plant was last watered {self.date}"
    
    class Meta:
        ordering = ('-date',)