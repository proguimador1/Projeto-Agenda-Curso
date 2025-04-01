from django.shortcuts import render
from contact.forms import ContactForm

def create(request):
    if request.method == 'POST':
        return render(
            request,
            'contact/create.html',
            {
                'form': ContactForm(data=request.POST),
                'site_title': 'Create contact',
            }
        )

    return render(
            request,
            'contact/create.html',
            {
                'form': ContactForm(),
                'site_title': 'Create contact',
            }
        )