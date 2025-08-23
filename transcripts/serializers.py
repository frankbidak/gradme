from rest_framework import serializers
from transcripts.models import Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source="course.name", read_only=True)
    grad_category = serializers.CharField(source="course.grad_category.name", read_only=True)

    class Meta:
        model = Enrollment
        fields = ["id", "term", "grade", "credits_earned", "course_name", "grad_category"]
