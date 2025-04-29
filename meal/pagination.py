from rest_framework.pagination import PageNumberPagination


class FoodPagination(PageNumberPagination):
    page_size = 5


class MealPagination(PageNumberPagination):
    page_size = 5