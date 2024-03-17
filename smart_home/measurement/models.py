from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=150)
    def __str__(self) -> str:
            return self.name
    
class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    

