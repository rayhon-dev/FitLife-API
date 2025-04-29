from django.urls import path
from . import views


urlpatterns = [
    path('foods/', views.FoodListCreateView.as_view(), name='list-create'),
    path('foods/<int:pk>/', views.FoodRetrieveUpdateDestroyView.as_view(), name='detail-update-delete'),
    path('meals/', views.MealListCreateView.as_view(), name='list-create'),
    path('meals/<int:pk>/', views.MealRetrieveUpdateDestroyView.as_view(), name='detail-update-delete')
]