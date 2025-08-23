from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ["id", "student_id", "grade_level", "cohort_year", "full_name"]

    def get_full_name(self, obj):
        return obj.user.get_full_name()
