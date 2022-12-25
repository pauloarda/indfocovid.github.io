from django import forms
from .models import Artikel

class ArtikelForms(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ('judul', 'body', 'kategory')
        widgets = {
            "judul" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type' : 'text',
                    'required' : True
                }),
            "body" : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'cols' : '30',
                    'rows' : '10',
                    'required' : True
                }),
            "kategory" : forms.Select(
                attrs={
                    'class': 'form-control selectpicker',
                    'required' : True,
                    'data-style':'btn btn-danger btn-block',
                    'title' : 'Pilih Kategori',
                    'data-size' : '7'
                }),

        }