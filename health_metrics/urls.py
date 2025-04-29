from django.urls import path
from . import views


urlpatterns = [
    path('health-metrics/', views.HealthMetricsListCreateView.as_view(), name='list-create'),
    path('health-metrics/<int:pk>/', views.HealthMetricsRetrieveUpdateDestroyView.as_view(), name='detail-update-delete')
]