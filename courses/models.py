from django.db import models
from schools.models import School
from requirements.models import RequirementCategory

class Course(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="courses")
    name = models.CharField(max_length=255)
    subject_area = models.CharField(max_length=100)  # descriptive label
    ag_category = models.CharField(max_length=2, blank=True, null=True)  # e.g. A, B, C ...
    credits = models.DecimalField(max_digits=5, decimal_places=2)  # e.g. 5.00
    grad_category = models.ForeignKey(
        RequirementCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="courses",
    )
    is_honors = models.BooleanField(default=False)
    is_ap = models.BooleanField(default=False)

    class Meta:
        unique_together = ("school", "name")

    def __str__(self):
        return f"{self.name} ({self.school.name})"
