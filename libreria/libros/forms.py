from dataclasses import fields
from django import forms
from .models import Author
from .models import Book

#Crear formulario
class AuthorForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Author

        #especificar los campos
        fields = [
            'first_name',
            'last_name',
            'photo',
            'birth_date'
        ]
class bookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields=[
            'name',
            'description',
            'year',
            'cost',
            'author'
        ]
