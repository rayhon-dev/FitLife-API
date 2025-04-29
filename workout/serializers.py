from rest_framework import serializers
from .models import Workout, Exercise, WorkoutExercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = [
            'id',
            'name',
            'description',
            'category',
            'calories_burned_per_hour'
        ]


class WorkoutExerciseInputSerializer(serializers.Serializer):
    exercise = serializers.IntegerField()
    sets = serializers.IntegerField()
    reps = serializers.IntegerField()
    weight = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)


class WorkoutExerciseOutputSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='exercise.id')
    name = serializers.CharField(source='exercise.name')

    class Meta:
        model = WorkoutExercise
        fields = ['id', 'name', 'sets', 'reps', 'weight']

class WorkoutSerializer(serializers.ModelSerializer):
    exercises = serializers.ListSerializer(
        child=WorkoutExerciseInputSerializer(), write_only=True
    )
    exercise_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'date', 'duration', 'exercises', 'exercise_details']

    def get_exercise_details(self, obj):
        return WorkoutExerciseOutputSerializer(
            obj.workout_exercises.select_related('exercise'), many=True
        ).data

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['exercises'] = rep.pop('exercise_details')
        return rep

    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises')
        workout = Workout.objects.create(user=self.context['request'].user, **validated_data)
        WorkoutExercise.objects.bulk_create([
            WorkoutExercise(
                workout=workout,
                exercise_id=item['exercise'],
                sets=item['sets'],
                reps=item['reps'],
                weight=item.get('weight')
            )
            for item in exercises_data
        ])
        return workout

    def update(self, instance, validated_data):
        exercises_data = validated_data.pop('exercises', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if exercises_data is not None:
            instance.workout_exercises.all().delete()
            WorkoutExercise.objects.bulk_create([
                WorkoutExercise(
                    workout=instance,
                    exercise_id=item['exercise'],
                    sets=item['sets'],
                    reps=item['reps'],
                    weight=item.get('weight')
                )
                for item in exercises_data
            ])

        return instance
