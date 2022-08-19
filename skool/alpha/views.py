from django.shortcuts import render

from django.http import HttpResponse
import os
from pathlib import Path
from alpha import subjectSections

def index(request):
    return render(request, 'base.html')
    

def Physics(request):
    content = {
        'sub_name' : 'Physics',
        'list_sections' : subjectSections.physicsSection,
    }
    return render(request,'physics.html', content)

def Maths(request):
    content = {
        'sub_name' : 'Maths',
        'list_sections' : subjectSections.mathsSection,
    }
    return render(request,'maths.html', content)

def Chemistry(request):
    content = {
        'sub_name' : 'Chemistry',
        'list_sections' : subjectSections.chemistrySection,
    }
    return render(request,'chemistry.html', content)

def Sections(request):
    return render(request, 'chemistry.html')




