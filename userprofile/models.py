from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'date_of_birth', 'gender']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_set_custom',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions_custom',
        blank=True
    )

    def __str__(self):
        return self.username




class UserProfile(models.Model):
    LEVEL_CHOICES = [
        ('sedentary', 'Sedentary'),
        ('lightly_active', 'Lightly active'),
        ('moderately_active', 'Moderately active'),
        ('very_active', 'Very active'),
        ('extra_active', 'Extra active')
    ]

    GOAL_CHOICES = [
        ('lose_weight', 'Lose weight'),
        ('maintain_weight', 'Maintain weight'),
        ('gain_weight', 'Gain weight'),
        ('build_muscle', 'Build muscle')
    ]


    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    activity_level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES)


    def __str__(self):
        return f"{self.user.email} Profile"