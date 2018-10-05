from django import forms
from .models import Piece, Person
import django_filters

class PieceFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    composer__surname = django_filters.CharFilter(lookup_expr='icontains')
    arranger__surname = django_filters.CharFilter(lookup_expr='icontains')
#    status=django_filters.CharFilter(widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Piece
#        fields = [ 'title', ]
        fields = [ 'title', 'composer__surname', 'arranger__surname', 'note', 'genre', 'feature', 'status', ]

class PersonFilter(django_filters.FilterSet):
    firstName = django_filters.CharFilter(lookup_expr='icontains')
    surname = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Person
        fields = [ 'surname', 'firstName','born','died','note', ]
