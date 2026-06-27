from django.shortcuts import render
from bio_app.models import Bio
from education_app.models import Education
from skills_app.models import Skill
from experience_projects_app.models import ProjectExperience

def index(request):
    bio = Bio.objects.first()
    education = Education.objects.all()
    skills = Skill.objects.all()
    projects = ProjectExperience.objects.exclude(item_type='experience')
    experiences = ProjectExperience.objects.filter(item_type='experience')

    # Fallback to prevent crashes if not seeded
    if not bio:
        bio = {
            'name': 'Alex Rivera',
            'job_title': 'MERN Stack Developer',
            'profile_picture': '/static/portfolio/images/profile.png',
            'description': 'A 21-year-old MERN stack developer specializing in the development of dynamic and interactive dashboards, associated with Webwaves Media. Passionate about building modern, responsive, and performance-driven web applications.'
        }

    context = {
        'bio': bio,
        'education_list': education,
        'skills_list': skills,
        'projects_list': projects,
        'experiences_list': experiences,
    }
    return render(request, 'portfolio/index.html', context)
