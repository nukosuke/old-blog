from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Entry
from .forms import EntryForm

from django.conf import settings
TOP_BANNER = settings.TOP_BANNER

def index(request):
    #TODO: make 5 to parameter
    """Return the last 5 published entries."""
    entries = Entry.objects.order_by('-published_at')[:5]
    return render(request, 'entry/index.html', {'TOP_BANNER': TOP_BANNER, 'entries': entries})

def show(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
    return render(request, 'entry/show.html', {'TOP_BANNER': TOP_BANNER, 'entry': entry})

@login_required
def new_edit(request):
    entry = Entry()
    form = EntryForm()
    return render(request, 'entry/new_edit.html', {'entry': entry, 'form': form})

@login_required
def edit(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
    form = EntryForm(instance=entry)
    return render(request, 'entry/edit.html', {'entry': entry, 'form': form})

@login_required
def new(request):
    entry_form = EntryForm(request.POST)
    entry = entry_form.save()
    return HttpResponseRedirect(reverse('entry-show', args=[entry.slug]))

@login_required
def update(request, entry_id):
    entry = Entry.objects.get(pk=entry_id)
    entry_form = EntryForm(request.POST, instance=entry)
    entry_form.save()
    return HttpResponseRedirect(reverse('entry-show', args=[entry.slug]))

@login_required
def delete(request, entry_id):
    entry = Entry.objects.get(pk=entry_id)
    entry.delete()
    return HttpResponseRedirect(reverse('entry-index'))
