from django.shortcuts import render
from . models import *
# Create your views here.
def home(request):
    profile=Profile.objects.all()
    skill=Skill.objects.all()
    education=Education.objects.all()
    experience=Experience.objects.all()
    project=Project.objects.all()
    certification=Certification.objects.all()

    page={
        'profile':profile,
        'skill':skill,
        'education':education,
        'experience':experience,
        'project':project,
        'certification':certification,
    }

    return render(request,'index.html',page)
