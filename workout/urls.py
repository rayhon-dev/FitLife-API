from django.urls import path
from . import views


urlpatterns = [
    path('exercises/', views.ExerciseListCreateView.as_view(), name='list-create'),
    path('exercises/<int:pk>/', views.ExerciseRetrieveUpdateDestroyView.as_view(), name='detail-update-delete'),
    path('workouts/', views.WorkoutListCreateView.as_view(), name='list-create'),
    path('workouts/<int:pk>/', views.WorkoutRetrieveUpdateDestroyView.as_view(), name='detail-update-delete')

]