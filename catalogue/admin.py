from django.contrib import admin

# Register your models here.
from .models import Piece, Person, Genre

admin.site.register(Piece)
admin.site.register(Person)
admin.site.register(Genre)

class PiecesInline(admin.TabularInline):
    """
    Defines format of inline piece insertion (used in PersonAdmin)
    """
    model = Piece

#@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """
    Administration object for Person models.
    Define:
     - fields to be displayed inlist view (list_display)
     - orders fields in detail view (fields), grouping date fields horizontally
     - adds inline addition of pieces in composer view (inlines)
    """
    list_display = ('surname', 'firstName')
    fields = ['firstName', 'surname']
    inlines = [PiecesInline]


