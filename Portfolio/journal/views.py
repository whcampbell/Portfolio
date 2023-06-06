from django.shortcuts import render
from django.views.generic import ListView
from .models import Entry

class EntryList(ListView) :
    model = Entry
    paginate_by = 4

def index(request) :
    entry = Entry.objects.first()
    return render(request, 'journal/index.html', {'entry':entry})

def entry_detail(request, pk) :
    entry = Entry.objects.get(pk=pk)
    return render(request, 'journal/entry.html', {'entry':entry})

# Create your views here.
