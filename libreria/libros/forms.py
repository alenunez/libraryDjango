from django import forms
from .models import Author

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