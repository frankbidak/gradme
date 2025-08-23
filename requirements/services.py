from collections import defaultdict
from decimal import Decimal
from students.models import Student
from requirements.models import RequirementCategory


def get_graduation_progress(student: Student):
    # Build requirement map for this school
    reqs = RequirementCategory.objects.filter(school=student.school)
    required = {r.name: r.credits_required for r in reqs}

    # Sum earned credits per category based on course.grad_category
    earned = defaultdict(Decimal)
    for e in student.enrollments.select_related("course__grad_category"):
        cat = e.course.grad_category.name if e.course.grad_category else "Electives"
        earned[cat] += e.credits_earned

    # Build friendly report
    report = []
    for name, needed in required.items():
        have = earned.get(name, Decimal("0"))
        report.append({
            "category": name,
            "required": float(needed),
            "earned": float(have),
            "remaining": float(max(Decimal("0"), needed - have)),
        })

    # Extra elective credits beyond mapped categories
    # (If you have an explicit Electives requirement row, it’s already covered.)

    total_required = float(sum(required.values()))
    total_earned = float(sum(e["earned"] for e in report))

    return {
        "by_category": report,
        "totals": {
            "required": total_required,
            "earned": total_earned,
            "remaining": max(0.0, total_required - total_earned),
        },
    }
