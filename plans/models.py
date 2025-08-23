from django.db import models
from students.models import Student
from courses.models import Course

class FourYearPlanItem(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="plan_items")
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    planned_year = models.IntegerField()  # 9, 10, 11, 12
    planned_term = models.CharField(max_length=16, blank=True, null=True)  # Fall/Spring

    class Meta:
        ordering = ["student", "planned_year", "planned_term"]
