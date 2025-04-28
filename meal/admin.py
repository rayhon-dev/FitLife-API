from django.contrib import admin
from .models import Food, Meal, MealFood


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'calories', 'protein', 'carbs', 'fats')
    search_fields = ('name',)


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'meal_type')
    list_filter = ('meal_type', 'date')
    search_fields = ('user__username',)


@admin.register(MealFood)
class MealFoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'meal', 'food', 'quantity')
    list_filter = ('meal', 'food')
