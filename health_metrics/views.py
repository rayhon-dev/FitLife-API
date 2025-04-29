from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .models import HealthMetrics
from .serializers import HealthMetricsSerializer
from .pagination import HealthMetricsPagination


class HealthMetricsListCreateView(generics.ListCreateAPIView):
    queryset = HealthMetrics.objects.all()
    serializer_class = HealthMetricsSerializer
    pagination_class = HealthMetricsPagination
    permission_classes = [IsAuthenticated]


class HealthMetricsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HealthMetrics.objects.all()
    serializer_class = HealthMetricsSerializer
    permission_classes = [IsAuthenticated , IsOwnerOrReadOnly]
    lookup_field = 'pk'
