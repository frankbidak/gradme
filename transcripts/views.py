from rest_framework import permissions, generics
from transcripts.models import Enrollment
from transcripts.serializers import EnrollmentSerializer

class StudentTranscriptView(generics.ListAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        student_id = self.kwargs["student_id"]
        qs = Enrollment.objects.select_related("course", "student").filter(student_id=student_id)
        user = self.request.user
        if user.is_superuser or user.groups.filter(name__in=["Admin", "Counselor"]).exists():
            return qs
        return qs.filter(student__user=user)
