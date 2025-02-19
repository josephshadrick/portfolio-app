from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project, Skill

class ProjectListView(ListView):
    model = Project
    template_name = "projects.html"
    context_object_name = "projects"

class ProjectDetailView(DetailView):
    model = Project
    template_name = "project_details.html"
    context_object_name = "project"

class SkillListView(ListView):
    model = Skill
    template_name = "skills.html"
    context_object_name = "skills"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Skill.objects.values("category").distinct()
        return context
    

def resume_view(request):
    return render(request, "home.html")