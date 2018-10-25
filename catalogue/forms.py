from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django import forms
from django.forms import ModelForm, TextInput, CharField, SelectMultiple
from django.contrib.auth.models import User
from .models import Piece

#class PieceUpdateForm(forms.Form):
class PieceUpdateForm(ModelForm):
    """
    Form to update details of a piece.
    """
    class Meta:
        model = Piece
        fields = ( 'title', 'note','composer',  'arranger', 'genre', 'feature', 'status' )
        widgets = {
		    'genre': SelectMultiple()
		}
    def __init__(self, *args, **kwargs):
        super(PieceUpdateForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = False
        self.fields['status'].required = False

class PieceSearchForm(ModelForm):
    composer=forms.CharField(widget=forms.TextInput())
    composer.required=False
    arranger=forms.CharField(widget=forms.TextInput())
    arranger.required=False
    """
    Form to update details of a piece.
    """
    class Meta:
        model = Piece
        fields = ( 'title', 'note','composer',  'arranger', 'genre', 'feature', 'status' )
        widgets = {
		    'genre': SelectMultiple()
		}
    def __init__(self, *args, **kwargs):
        super(PieceSearchForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = False
        self.fields['status'].required = False

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
