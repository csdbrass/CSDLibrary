from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#  Create your views here.

from .models import Piece, Person, Genre
from .forms import PieceUpdateForm
from .filters import PieceFilter, PersonFilter

def index(request):
    """
    View function for site's home page
    """
    num_visits=request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'index.html', context={'num_visits':num_visits})

def search(request):
    piece_list = Piece.objects.all()
    piece_filter = PieceFilter(request.GET, queryset=piece_list)  
#    if user.is_staff(): 
    return render(request, 'search/pieceUpdate1.html', {'filter': piece_filter})
#    else:
#        return render(request, 'search/pieceList1.html', {'filter': piece_filter})
	
def searchPerson(request):
    person_list = Person.objects.all()
    person_filter = PersonFilter(request.GET, queryset=person_list)
    return render(request, 'search/personUpdate.html', {'filter': person_filter})

def searchList(request):
    piece_list = Piece.objects.all()
    piece_filter = PieceFilter(request.GET, queryset=piece_list)
    return render(request, 'search/pieceUpdateList.html', {'filter': piece_filter})

def PieceSearch(request):
    piece_list = Piece.objects.all()
    piece_filter = PieceFilter(request.GET, queryset=piece_list)
    return render(request, 'search/pieceSearch.html', {'filter': piece_filter})

def PieceSearchList(request):
    if request.method == "POST":
        form = PieceUpdateForm(request.POST, instance=piece)
        if form.has_changed():
            if form.is_valid():   
                piece = form.save()
            else:
                pass    # erroneous form
        return redirect('pieceEditList', pk=piece.pk+1)
    else:
        piece_list = Piece.objects.all()
        piece_filter = PieceFilter(request.GET, queryset=piece_list)
        return render(request, 'search/pieceSearch.html', {'filter': piece_filter})
	
def PieceEdit(request, pk):
    piece = get_object_or_404(Piece, pk=pk)
	
    if request.method == "POST":
        form = PieceUpdateForm(request.POST, instance=piece)
        if form.is_valid():
            piece = form.save()
            return redirect('piece-detail', pk=piece.pk)
    else:
        form = PieceUpdateForm(instance=piece)
    return render(request, 'search/pieceUpdate.html', {'form': form})	

def PieceEditList(request, pk):
    piece = get_object_or_404(Piece, pk=pk)
	
    if request.method == "POST":
        form = PieceUpdateForm(request.POST, instance=piece)
        if form.has_changed():
            if form.is_valid():   
                piece = form.save()
            else:
                pass    # erroneous form
        return redirect('pieceEditList', pk=piece.pk+1)
    else:
        form = PieceUpdateForm(instance=piece)
    return render(request, 'search/pieceUpdate.html', {'form': form})	

def findPiece(request):
    return render(request, 'findPiece.html')

def addPerson(request):
    return render(request, 'search/personUpdate.html')

def addPiece(request):
    if request.method == "POST":
        form = PieceUpdateForm(request.POST,)
        if form.is_valid():
            piece = form.save()
            return redirect('piece-detail', pk=piece.pk)
    else:
        form = PieceUpdateForm()
    return render(request, 'search/pieceUpdate.html', {'form': form})	
	
def PieceUpdateView(request):
    """
    Edit the details for a piece
    """
    composers= Person.objects.all()
   
    return render(request, 'pieceUpdate.html')

def listComposers(request):
    """
    List all composers in the database
    """
    composers = Person.objects.all()
    comp_filter = PersonFilter(request.GET, queryset=composers)
    return render(request, 'listComposer.html', {'filter':comp_filter})

class PieceListView(generic.ListView):
    model = Piece

class PieceDetailView(generic.DetailView):
    model = Piece

class PersonListView(generic.ListView):
    model = Person

class PersonDetailView(generic.DetailView):
    model = Person 

class ComposerListView(generic.ListView):
    model = Person

class ComposerDetailView(generic.DetailView):
    model = Person 

class ArrangerListView(generic.ListView):
    model = Person

class ArrangerDetailView(generic.DetailView):
    model = Person 

#from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Person


#class PersonCreate(PermissionRequiredMixin, CreateView):
class PersonCreate(CreateView):
    model = Person
#    fields = '__all__'
    fields =  ['firstName','surname','born','died','note']
    template_name='search/personCreate.html'
#    permission_required = 'catalogue.can_mark_returned'


#class PersonUpdate(PermissionRequiredMixin, UpdateView):
class PersonUpdate(UpdateView):
    model = Person
#    fields = '__all__'
    fields =  ['firstName','surname','born','died','note']
    template_name='search/personUpdate1.html'
#    fields = ['firstName','surname',]
#    permission_required = 'catalogue.can_mark_returned'
#    success_url = reverse_lazy('personUpdate')
	
#class PersonDelete(PermissionRequiredMixin, DeleteView):
class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('persons')
#    permission_required = 'catalogue.can_mark_returned'


#class PieceCreate(PermissionRequiredMixin, CreateView):
class PieceCreate(CreateView):
    model = Piece
    fields = '__all__'
    template_name='search/pieceCreate.html'
#    permission_required = 'catalogue.can_mark_returned'

#class PieceUpdate(PermissionRequiredMixin, UpdateView):
class PieceUpdate(UpdateView):
    model = Piece
    fields = '__all__'
#    permission_required = 'catalogue.can_mark_returned'

#class PieceDelete(PermissionRequiredMixin, DeleteView):
class PieceDelete(DeleteView):
    model = Piece
    success_url = reverse_lazy('pieces')
#    permission_required = 'catalogue.can_mark_returned'


def userLogin(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details!")
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'userLogin.html', {})
		
# Use the login_required() decorator to ensure only those logged in can access the view.

@login_required
def userLogout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')