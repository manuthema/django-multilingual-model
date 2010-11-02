from django.db import models

from multilingual_model.models import MultilingualModel, MultilingualTranslation

class BookTranslation(MultilingualTranslation):
    title = models.CharField(max_length=32)
    description = models.TextField()
    model = models.ForeignKey('Book')

class Book(MultilingualModel):
    ISBN = models.IntegerField()

    class Meta:
        translation = BookTranslation
        multilingual = ['title', 'description']

__test__ = {'doctest': """
>>> book = Book(ISBN="1234567890")
>>> book.save()
>>> book_en = BookTranslation()
>>> book_en.title = "Django for Dummies"
>>> book_en.description = "Django described in simple words."
>>> book_en.model = book
>>> book_en.save()
>>> book_pl = BookTranslation()
>>> book_pl.title = "Django dla Idiotow"
>>> book_pl.description = "Django opisane w prostych slowach"
>>> book_pl.model = book
>>> book_pl.save()
>>> # now here comes the magic
>>> book.title_en
u'Django for Dummies'
>>> book.description_pl
u'Django opisane w prostych slowach'
"""}