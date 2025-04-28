from django.db import models
from userprofile.models import User


class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)
    fats = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Meal(models.Model):
    MEAL_TYPE_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')
    date = models.DateField()
    meal_type = models.CharField(max_length=10, choices=MEAL_TYPE_CHOICES)
    foods = models.ManyToManyField(Food, through='MealFood')

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.meal_type}"

class MealFood(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='meal_food')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='food_meals')
    quantity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.meal} - {self.food} x {self.quantity}"
