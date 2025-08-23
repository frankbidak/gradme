from django.contrib import admin
from django.urls import path
from students.views import StudentDetailView
from transcripts.views import StudentTranscriptView
from requirements.views import StudentProgressView

urlpatterns = [
    path("admin/", admin.site.urls),

    # API
    path("api/students/<int:pk>/", StudentDetailView.as_view()),
    path("api/students/<int:student_id>/transcript/", StudentTranscriptView.as_view()),
    path("api/students/<int:student_id>/progress/", StudentProgressView.as_view()),
]
