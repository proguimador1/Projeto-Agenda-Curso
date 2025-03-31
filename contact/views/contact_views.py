from django.shortcuts import render, get_object_or_404
from contact.models import Contact

def home(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')
    return render(
            request,
            'contact/index.html',
            {
                'contacts': contacts
            }
        )

def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id)
    return render(
            request,
            'contact/contact.html',
            {
                'contact': single_contact
            }
        )