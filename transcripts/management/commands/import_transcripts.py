import csv
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from schools.models import School
from students.models import Student
from requirements.models import RequirementCategory
from courses.models import Course
from transcripts.models import Enrollment

class Command(BaseCommand):
    help = "Import transcript CSV"

    def add_arguments(self, parser):
        parser.add_argument("csv_path", type=str)
        parser.add_argument("school_name", type=str)

    def handle(self, *args, **opts):
        path = opts["csv_path"]
        school_name = opts["school_name"]
        school, _ = School.objects.get_or_create(name=school_name)

        with open(path, newline='', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            required_cols = {"student_id", "first_name", "last_name", "grade_level", "cohort_year", "course_name", "subject_area", "grad_category", "credits", "term", "grade"}
            if not required_cols.issubset(reader.fieldnames):
                raise CommandError(f"CSV missing columns: {required_cols - set(reader.fieldnames)}")

            for row in reader:
                user, _ = User.objects.get_or_create(
                    username=row["student_id"],
                    defaults={
                        "first_name": row["first_name"],
                        "last_name": row["last_name"],
                        "email": "",
                    },
                )
                student, _ = Student.objects.get_or_create(
                    user=user,
                    defaults={
                        "school": school,
                        "student_id": row["student_id"],
                        "grade_level": int(row["grade_level"] or 9),
                        "cohort_year": int(row["cohort_year"] or 2028),
                    },
                )

                if student.school_id != school.id:
                    student.school = school
                    student.save()

                grad_cat = None
                if row["grad_category"]:
                    grad_cat, _ = RequirementCategory.objects.get_or_create(
                        school=school,
                        name=row["grad_category"],
                        defaults={"credits_required": 0},
                    )

                course, _ = Course.objects.get_or_create(
                    school=school,
                    name=row["course_name"],
                    defaults={
                        "subject_area": row["subject_area"],
                        "credits": float(row["credits"] or 5),
                        "grad_category": grad_cat,
                    },
                )
                if course.grad_category is None and grad_cat is not None:
                    course.grad_category = grad_cat
                    course.save()

                Enrollment.objects.create(
                    student=student,
                    course=course,
                    term=row["term"],
                    grade=row["grade"] or None,
                )

        self.stdout.write(self.style.SUCCESS("Import complete."))
