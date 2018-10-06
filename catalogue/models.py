from django.db import models

# Create your models here.

from django.urls import reverse #Used to generate urls by reversing the URL patterns

class Person(models.Model):
    firstName = models.CharField(max_length=200, blank=True, help_text="Enter individual's personal name")
    surname = models.CharField(max_length=200, help_text="Enter individual's family name")
    born = models.DateField(null=True, blank=True);
    died = models.DateField(null=True, blank=True);
    note = models.TextField(max_length=1000, blank=True, help_text="Enter any noteworthy information")

    def __str__(self):
        return '{0}, {1}'.format(self.surname,self.firstName) 

    class Meta:
        ordering = ['surname','firstName']

    def display_firstName(self):
        return (self.firstName)

    def display_surname(self):
        return (self.surname)

    def display_born(self):
        return (self.born)

    def display_surname(self):
        return (self.died)
	
    def get_absolute_url(self):
        return reverse('person-detail', args=[str(self.id)])

class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre-detail', args=[str(self.id)])

class Piece(models.Model):
    """
    Model represent a piece of music
    """
    ISSUED = 'IS'
    INSTORE = 'ST'
    DISCARDED = 'DD'
    MISSING = 'LO'
    STATUS_CHOICES = (
      (ISSUED, 'Issued'),
      (INSTORE, 'Stored'),
      (DISCARDED, 'Discarded'),
      (MISSING, 'Missing'),
    )

    SOPRANO = 'sop'
    CORNET  = 'crn'
    FLUGEL  = 'flg'
    TENOR   = 'tnr'
    BRTN    = 'brt'
    EUPH    = 'eu'
    TRMBN   = 'tbn'
    BSTBN   = 'btb'
    EBASS   = 'efb'
    BBASS   = 'bfb'
    DRUMKIT = 'kit'
    TIMPS   = 'tmp'

    INSTRUMENTS = (
      (SOPRANO, 'soprano'),
      (CORNET, 'cornet'),
      (FLUGEL, 'flugel horn'),
      (TENOR, 'tenor horn'),
      (BRTN, 'baritone'),
      (EUPH, 'euphonium'),
      (TRMBN, 'trombone'),
      (BSTBN, 'bass trombone'),
      (EBASS, 'e-flat bass'),
      (BBASS, 'b-flat bass'),
      (DRUMKIT, 'drum kit'),
      (TIMPS, 'timpani'),
    )

    title = models.CharField(max_length=200, help_text="Enter the title of the piece")
    note = models.TextField(max_length=1000, blank=True, help_text="Enter any noteworthy information about the piece")
    composer = models.ManyToManyField(Person, blank=True, help_text="Select one or more names")
    arranger = models.ManyToManyField(Person, related_name='arranger', blank=True, help_text="Select one or more names")
    genre = models.ManyToManyField(Genre, blank=True, help_text="Select one or more genres")
    feature = models.CharField(max_length=3, choices=INSTRUMENTS, blank=True, help_text="Select solo instrument")
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=INSTORE)

    class Meta:
	    ordering = ('title',)
    
    def __str__(self):
        """
        string for representing the piece
        """
        return self.title

    def display_composer(self):
        rv = ''
        for c in self.composer.all():
            if rv:
                rv += ', '
            rv = rv + c.firstName + ' ' + c.surname
			
        return rv
	
#        return ', '.join( composer.surname for composer in self.composer.all()[:3])

    def display_arranger(self):
        rv = ''
        for c in self.arranger.all():
            if rv:
                rv += ', '
            rv = rv + c.firstName + ' ' + c.surname
			
        return rv

#        return ', '.join( arranger.surname for arranger in self.arranger.all()[:3])

    def display_note(self):
        return (self.note)

    def display_genre(self):
        return ', '.join( genre.name for genre in self.genre.all()[:3])

    def display_feature(self):
        return (self.feature)

    def display_status(self):
        rv=" "
        for item in self.STATUS_CHOICES:
            if item[0] == self.status:
                rv=item[1]
                break
        return rv
		
    def get_absolute_url(self):
        return reverse('piece-detail', args=[str(self.id)])
