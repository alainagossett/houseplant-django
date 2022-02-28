from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
class Accessory(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accessory_detail', kwargs={'pk': self.id})


class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=280)
    sunlight = models.CharField(max_length=100)
    water = models.CharField(max_length=100)
    issues = models.CharField(max_length=100)
    accessories = models.ManyToManyField(Accessory)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})



class Watering(models.Model):
    date = models.DateField('watering date')
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"Plant was last watered {self.date}"
    
    class Meta:
        ordering = ('-date',)
