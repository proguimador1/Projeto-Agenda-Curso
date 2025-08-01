from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from contact.forms import ContactForm
from contact.models import Contact
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def create(request):
    form_action = reverse('create')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
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

@login_required(login_url='login')
def update(request, contact_id):
    form_action = reverse('update', args=(contact_id,))
    contact = get_object_or_404(
                Contact, 
                id=contact_id,
                owner = request.user)

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)

        if form.is_valid():
            form.save()
            return redirect('home')

        return render(
            request,
            'contact/create.html',
            {
                'form': form,
                'form_action': form_action,
                'site_title': 'Edit contact',
            }
        )

    return render(
            request,
            'contact/create.html',
            {
                'form': ContactForm(instance=contact),
                'form_action': form_action,
                'site_title': 'Edit contact',
            }
        )

@login_required(login_url='login')
def delete(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id) 

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('home')

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'site_title': contact.__str__,
            'confirmation': confirmation,
        }
    )
