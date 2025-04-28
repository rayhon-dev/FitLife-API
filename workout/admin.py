from django.contrib import admin
from .models import Exercise, Workout, WorkoutExercise


class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'duration')
    inlines = [WorkoutExerciseInline]
    list_filter = ('user', 'date')


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'calories_burned_per_hour')
    list_filter = ('category',)


class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ('workout', 'exercise', 'sets', 'reps', 'weight')
    list_filter = ('workout', 'exercise')


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(WorkoutExercise, WorkoutExerciseAdmin)
