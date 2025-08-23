from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from students.models import Student
from .serializers import ProgressSerializer
from .services import get_graduation_progress

class StudentProgressView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, student_id):
        student = Student.objects.select_related("school", "user").get(id=student_id)
        user = request.user
        if not (user.is_superuser or user.groups.filter(name__in=["Admin", "Counselor"]).exists() or student.user_id == user.id):
            return Response({"detail": "Forbidden"}, status=403)
        data = get_graduation_progress(student)
        return Response(ProgressSerializer(data).data)
