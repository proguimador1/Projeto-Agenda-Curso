from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
    
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email',\
        'username',

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('This email is alredy used', code='invalid'),
            )

        return email
    
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)

    password1 = forms.CharField(

        label="Password",

        strip=False,

        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),

        help_text=password_validation.password_validators_help_text_html(),

        required=False,

    )

    password2 = forms.CharField(

        label="Repeat password",

        strip=False,

        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),

        help_text='Use the same password as before.',

        required=False,

    )
    
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email',\
        'username', 

    def save(self, commit=True):

        cleaned_data = self.cleaned_data

        user = super().save(commit=False)

        password = cleaned_data.get('password1')

        if password:

            user.set_password(password)

        if commit:

            user.save()

        return user

    def clean(self):

        password1 = self.cleaned_data.get('password1')

        password2 = self.cleaned_data.get('password2')

        if password1 or password2:


            if password1 != password2:

                self.add_error(
                    'password2',

                    ValidationError('Enter the same password')
                )

        return super().clean()

    def clean_email(self):

        email = self.cleaned_data.get('email')

        current_email = self.instance.email

        if current_email != email:

            if User.objects.filter(email=email).exists():

                self.add_error(

                    'email',

                    ValidationError('Já existe este e-mail', code='invalid')

                )

        return email

    def clean_password1(self):

        password1 = self.cleaned_data.get('password1')

        if password1:

            try:

                password_validation.validate_password(password1)

            except ValidationError as errors:

                self.add_error(

                    'password1',

                    ValidationError(errors)

                )

        return password1