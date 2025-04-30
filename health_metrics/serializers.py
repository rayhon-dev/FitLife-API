from rest_framework import serializers
from .models import HealthMetrics


class HealthMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthMetrics
        fields = '__all__'
        read_only_fields = ['user']