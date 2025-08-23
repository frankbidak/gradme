from django.db import models
from students.models import Student
from courses.models import Course

PASSING_GRADES = {"A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "P"}

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name="enrollments")
    term = models.CharField(max_length=32)  # e.g. "Fall 2024"
    grade = models.CharField(max_length=5, blank=True, null=True)
    credits_earned = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if self.grade and self.grade.upper() in PASSING_GRADES:
            self.credits_earned = self.course.credits
        else:
            self.credits_earned = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} – {self.course} ({self.term})"
