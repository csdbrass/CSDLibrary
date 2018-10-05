from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
    
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Piece

#class PieceUpdateForm(forms.Form):
class PieceUpdateForm(ModelForm):
    """
    Form to update details of a piece.
    """
    class Meta:
        model = Piece
#        fields = '__all__'
        fields = ( 'title', 'note', 'composer', 'arranger', 'genre', 'feature', 'status' )

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')		
		