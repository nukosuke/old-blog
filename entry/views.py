from django.shortcuts import render
from .models import Entry

def index(request):
    entries = []
    return render(request, 'entry/index.html', {})

def show(request, entry_id):
    entry = {}
    return render(request, 'entry/show.html', {})
