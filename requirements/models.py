from django.db import models
from schools.models import School

class RequirementCategory(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="requirement_categories")
    name = models.CharField(max_length=100)  # e.g. English, Math, VPA
    credits_required = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ("school", "name")

    def __str__(self):
        return f"{self.school.name} – {self.name} ({self.credits_required})"

# Create your models here.
