from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Entry

def index(request):
    #TODO: make 5 to parameter
    """Return the last 5 published entries."""
    entries = Entry.objects.order_by('-published_at')[:5]
    return render(request, 'entry/index.html', {'entries': entries})

def show(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
    return render(request, 'entry/show.html', {'entry': entry})

@login_required
def edit(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'entry/edit.html', {'entry': entry})

@login_required
def new(request):
    return #TODO:redirect
