from django.shortcuts import render, redirect
from contact.forms import ContactForm

def create(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

        return render(
            request,
            'contact/create.html',
            {
                'form': form,
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