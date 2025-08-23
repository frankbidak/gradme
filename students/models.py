from django.db import models
from django.contrib.auth.models import User
from schools.models import School

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="students")
    student_id = models.CharField(max_length=50, unique=True)
    grade_level = models.IntegerField()
    cohort_year = models.IntegerField()  # expected grad year

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.student_id})"
