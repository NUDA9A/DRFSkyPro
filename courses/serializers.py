from rest_framework import serializers

from courses.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['name', 'description', 'preview', 'user', 'lesson_count']

    @staticmethod
    def get_lesson_count(course):
        return Lesson.objects.filter(course=course).count()
