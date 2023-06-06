from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from .models import Entry, Comment
from .forms import CommentForm

class EntryList(ListView) :
    model = Entry
    paginate_by = 4

class EntryDetail(View) :
    template_name = 'journal/entry.html'
    form_class = CommentForm

    def get(self, request, pk) :
        entry = Entry.objects.get(pk=pk)
        form = self.form_class()
        context = {
            'entry':entry,
            'form':form,
        }
        return render(request, self.template_name, context)    
    
    def post(self, request, pk) :
        entry = Entry.objects.get(pk=pk)
        form = self.form_class(request.POST)
        if (form.is_valid()) :
            body = form.cleaned_data['body']
            Comment.objects.create(
                user = request.user,
                entry = entry,
                body = body,
            )
            form = self.form_class
        else :
            form.add_error('body', 'Comment not valid, somehow')

        context = {
            'entry':entry,
            'form':form,
        }
        return render(request, self.template_name, context)
        


def index(request) :
    entry = Entry.objects.first()
    return render(request, 'journal/index.html', {'entry':entry})


# Create your views here.
