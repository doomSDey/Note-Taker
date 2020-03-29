from django.shortcuts import render,redirect,get_object_or_404
from django.template import RequestContext, loader
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm

# Create your views here.
#The view function for rendering the Main notes.html(Home Page)
def index(request):
    all_notes = Note.objects.all()
    return render(request, 'Notes/notes.html',{'Notes':all_notes})
    #return render_to_response("note.html", notes)

#function for adding a new note
def add_notes(request):
    note_title=request.POST["note_title"]
    note_text=request.POST["note_text"]
    note_color=request.POST["radio"]
    note=Note(text=note_text,title=note_title,color=note_color)
    note.save()
    return redirect('../notes')

#function for deleting a note
def delete(request,id):
     if request.method == 'POST':
        form=NoteForm()
        inventory = Note.objects.all()
        #item_id = request.POST.get(title=i)
        item_id = get_object_or_404(Note,title=id)
        #item = Note.objects.filter(title=id)
        item_id.delete()
        return redirect(reverse_lazy(index))
