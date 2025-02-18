from django.urls import path

from .views import ProjectListView, ProjectDetailView, SkillListView, resume_view

urlpatterns = [
    path("", resume_view, name="home"),
    path("projects/", ProjectListView.as_view(), name="projects"),
    path("skills/", SkillListView.as_view(), name="skills"),
    path("projects/<int:pk>", ProjectDetailView.as_view(), name="project_details"),
]