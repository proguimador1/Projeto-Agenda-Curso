from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from contact.forms import ContactForm
from contact.models import Contact

def create(request):
    form_action = reverse('create')

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
                'form_action': form_action,
                'site_title': 'Create contact',
            }
        )

    return render(
            request,
            'contact/create.html',
            {
                'form': ContactForm(),
                'form_action': form_action,
                'site_title': 'Create contact',
            }
        )

def update(request, contact_id):
    form_action = reverse('update', args=(contact_id,))
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == 'POST':
        form = ContactForm(data=request.POST, instance=contact)

        if form.is_valid():
            form.save()
            return redirect('home')

        return render(
            request,
            'contact/create.html',
            {
                'form': form,
                'form_action': form_action,
                'site_title': 'Create contact',
            }
        )

    return render(
            request,
            'contact/create.html',
            {
                'form': ContactForm(instance=contact),
                'form_action': form_action,
                'site_title': 'Create contact',
            }
        )