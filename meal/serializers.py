from rest_framework import serializers
from .models import Food, MealFood, Meal


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'id',
            'name',
            'calories',
            'protein',
            'carbs',
            'fats'
        ]


class MealFoodOutputSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='food.id')
    name = serializers.CharField(source='food.name')

    class Meta:
        model = MealFood
        fields = ['id', 'name', 'quantity']


class MealFoodInputSerializer(serializers.Serializer):
    food = serializers.IntegerField()
    quantity = serializers.DecimalField(max_digits=5, decimal_places=2)


class MealSerializer(serializers.ModelSerializer):
    foods = MealFoodInputSerializer(many=True, write_only=True)
    foods_output = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Meal
        fields = ['id', 'date', 'meal_type', 'foods', 'foods_output']

    def get_foods_output(self, obj):
        return MealFoodOutputSerializer(
            obj.meal_food.select_related('food'), many=True
        ).data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['foods'] = data.pop('foods_output')
        return data

    def create(self, validated_data):
        foods_data = validated_data.pop('foods')
        meal = Meal.objects.create(user=self.context['request'].user, **validated_data)

        meal_foods = []
        for item in foods_data:
            if not Food.objects.filter(id=item['food']).exists():
                raise serializers.ValidationError(f"Food with id {item['food']} does not exist.")
            meal_foods.append(MealFood(
                meal=meal,
                food_id=item['food'],
                quantity=item['quantity']
            ))

        MealFood.objects.bulk_create(meal_foods)
        return meal

    def update(self, instance, validated_data):
        foods_data = validated_data.pop('foods', None)

        # Oddiy field'larni yangilash
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Agar yangi foods kelgan bo‘lsa, eski ma'lumotlarni o‘chirib, yangilarini qo‘shamiz
        if foods_data is not None:
            instance.meal_food.all().delete()
            new_meal_foods = []
            for item in foods_data:
                if not Food.objects.filter(id=item['food']).exists():
                    raise serializers.ValidationError(f"Food with id {item['food']} does not exist.")
                new_meal_foods.append(MealFood(
                    meal=instance,
                    food_id=item['food'],
                    quantity=item['quantity']
                ))
            MealFood.objects.bulk_create(new_meal_foods)

        return instance
