from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact

def number_in_name_validation(name):
    if any(c.isdigit() for c in name):
            raise ValidationError(
                'Name cannot contain numbers',
                code='invalid'
                )

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

        self.fields['picture'] = forms.ImageField(
            widget=forms.FileInput(
               attrs={
                  'accept': 'image/*',
             }
            )
        )

    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'phone', 'email',\
                'description', 'category', 'picture',

    def clean(self):
        cleaned_data = self.cleaned_data

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                "First and last name cannot be the same",
                code='invalid'
            )

            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        number_in_name_validation(first_name)

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        number_in_name_validation(last_name)

        return last_name
    
    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        
        if len(phone) < 11:
            raise ValidationError(
                "Plase, enter a valid phone number",
                code='invalid'
            )

        return phone
    
    