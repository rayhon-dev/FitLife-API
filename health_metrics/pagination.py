from rest_framework.pagination import PageNumberPagination


class HealthMetricsPagination(PageNumberPagination):
    page_size = 5