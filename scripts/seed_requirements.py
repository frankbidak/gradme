from django.contrib.auth import get_user_model
from schools.models import School
from requirements.models import RequirementCategory

def run():
    school, _ = School.objects.get_or_create(name="Magnolia Science Academy High School")
    defaults = {
        "English": 40,
        "Mathematics": 30,
        "Science": 30,
        "History/Social Science": 30,
        "World Language": 20,
        "Visual & Performing Arts": 10,
        "Physical Education": 20,
        "Electives": 70,
    }
    for name, creds in defaults.items():
        RequirementCategory.objects.get_or_create(
            school=school, name=name, defaults={"credits_required": creds}
        )
