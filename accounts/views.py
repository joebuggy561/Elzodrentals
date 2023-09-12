from django.shortcuts import render
from django.shortcuts import render
from .models import Register




def register(request):
    if request.method == 'POST':
        form = Register()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        country = request.POST.get('country')
        form.name = name
        form.email = email
        form.country = country 
        form.phone_number = phone_number
        form.save()
       
           
        return render(request, 'home.html')
    else:
        form = Register()
    return render(request, 'home.html')
