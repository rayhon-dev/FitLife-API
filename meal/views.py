from rest_framework import generics
from .models import Food, Meal
from .pagination import FoodPagination, MealPagination
from .serializers import FoodSerializer, MealSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class FoodListCreateView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    pagination_class = FoodPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['calories', 'protein', 'carbs', 'fats']
    ordering_fields = ['calories', 'protein', 'carbs', 'fats']


    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsAdminUser()]
        return [IsAuthenticated()]


class FoodRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), IsAdminUser()]
        return [IsAuthenticated()]

class MealListCreateView(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    pagination_class = MealPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['meal_type', 'date']
    ordering_fields = ['date']


class MealRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated , IsOwnerOrReadOnly]
    lookup_field = 'pk'


