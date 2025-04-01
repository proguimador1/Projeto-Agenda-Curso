from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Ex: Joaquim'
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Ex: da Silva'
        })
        self.fields['phone'].widget.attrs.update({
            'placeholder': 'Ex: (00)00000-0000'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Ex: fulanotal@email.com'
        })
        self.fields['description'].widget.attrs.update({
            'placeholder': 'A short description of the contact',
            'style': 'max-height: 10rem;max-width: 80rem;resize: none'
        })

    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'phone', 'email',\
                'description', 'category', 'picture',

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Error message',
                code='invalid'
            )
        )

        return super().clean()