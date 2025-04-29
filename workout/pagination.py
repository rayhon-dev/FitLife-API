from rest_framework.pagination import PageNumberPagination


class WorkoutPagination(PageNumberPagination):
    page_size = 5

class ExercisePagination(PageNumberPagination):
    page_size = 5