from django.db import models
from userprofile.models import User


class HealthMetrics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='health_metrics')
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    body_fat_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    blood_pressure_systolic = models.PositiveIntegerField(null=True, blank=True)
    blood_pressure_diastolic = models.PositiveIntegerField(null=True, blank=True)
    heart_rate = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.date}"
