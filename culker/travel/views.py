from django.shortcuts import render
from django.http import HttpResponse
from travel.models import *

def index(request):
    features = Seed.objects.filter(feature=True)    
    return render(request, 'index.html', {'feature': features})

def about(request):
    return render(request, 'about.html', {})

def help(request):
    return render(request, 'help.html', {})

def list(request):
    seeds = Seed.objects.all()
    return render(request, 'list.html', {'seeds': seeds})

def seed(request, seed_id):
    seed = Seed.objects.get(pk=seed_id)
    his_trips = Trip.objects.filter(seed_id=seed_id)
    return render(request, 'project.html', {'seed': seed, 'his_trips': his_trips})

def story(request, story_id):
    story = Trip.objects.get(pk=story_id)
    notes = story.note.split('@')
    timetable = story.timetable.split('@')
    return render(request, 'story.html', {'story': story, 'notes': notes, 'timetable': timetable})
