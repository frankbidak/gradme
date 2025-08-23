from rest_framework import permissions, generics
from students.models import Student
from students.serializers import StudentSerializer

class StudentDetailView(generics.RetrieveAPIView):
    queryset = Student.objects.select_related("user")
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.is_superuser or user.groups.filter(name__in=["Admin", "Counselor"]).exists():
            return qs
        # Students can only view themselves
        return qs.filter(user=user)
