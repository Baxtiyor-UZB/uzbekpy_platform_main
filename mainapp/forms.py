from mainapp.models import Contact
from django import forms

class MyCommentForm(forms.ModelForm):
    class Meta(object):
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control'
                     }
                ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control'
                    }
                 ),
             }    