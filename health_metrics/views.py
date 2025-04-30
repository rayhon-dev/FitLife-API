from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .models import HealthMetrics
from .serializers import HealthMetricsSerializer
from .pagination import HealthMetricsPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class HealthMetricsListCreateView(generics.ListCreateAPIView):
    queryset = HealthMetrics.objects.all()
    serializer_class = HealthMetricsSerializer
    pagination_class = HealthMetricsPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = [
        'date',
        'weight',
        'body_fat_percentage',
        'blood_pressure_systolic',
        'blood_pressure_diastolic',
        'heart_rate'
    ]
    ordering_fields = [
        'date',
        'weight',
        'heart_rate'
    ]

    def get_queryset(self):
        return HealthMetrics.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HealthMetricsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HealthMetrics.objects.all()
    serializer_class = HealthMetricsSerializer
    permission_classes = [IsAuthenticated , IsOwnerOrReadOnly]
    lookup_field = 'pk'
