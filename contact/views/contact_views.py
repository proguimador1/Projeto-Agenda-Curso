from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact

def home(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')
    return render(
            request,
            'contact/index.html',
            {
                'contacts': contacts,
                'site_title': 'Agenda',
            }
        )

def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id)
    return render(
            request,
            'contact/contact.html',
            {
                'contact': single_contact,
                'site_title': single_contact.__str__,
            }
        )

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('home')

    contacts = Contact.objects.filter(show=True)\
    .filter(
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(email__icontains=search_value) 
    )\
    .order_by('-id')
    return render(
            request,
            'contact/index.html',
            {
                'contacts': contacts,
                'site_title': 'Agenda',
                'search_value': search_value,
            }
        )