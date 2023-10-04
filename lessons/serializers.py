from rest_framework import serializers
from lessons.models import Lesson, Product, ViewDetail


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name', 'url', 'duration']


class ViewDetailSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()

    class Meta:
        model = ViewDetail
        fields = ['lesson', 'watched', 'status', 'when_watched']


class ProductSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'lessons']


class ProductDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    sum_seconds = serializers.IntegerField()
    people_watched = serializers.IntegerField()
    num_students = serializers.IntegerField()
