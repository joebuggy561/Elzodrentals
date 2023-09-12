from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from . models import Contact

def contact(request):
    if request.method == 'POST':
        contact = Contact()
        contact_name = request.POST.get('name')
        contact_email = request.POST.get('email')
        contact_message = request.POST.get('message')
        contact.name = contact_name
        contact.email = contact_email
        contact.message = contact_message 
        contact.save()
        messages.success(request, 'Thank you for Contacting Us. One of our Agents will get to you in the next 24-48hrs')
        return render(request, 'home.html')
    else:
        contact = Contact()
    messages.error(request, "This is a bad information please Enter the right Data")
    return render(request, 'home.html')