from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from . models import Bookings

def bookings(request):
    if request.method == 'POST':
        bookings = Bookings()
        bookings_p_location = request.POST.get('p_location')
        bookings_d_location = request.POST.get('d_location')
        bookings_p_date = request.POST.get('p_date', "%Y-%m-%dT%H:%M")
        bookings_d_date = request.POST.get('d_date', "%Y-%m-%dT%H:%M")
        bookings_p_up_time = request.POST.get('p_up_time')
        bookings.p_location = bookings_p_location
        bookings.d_location = bookings_d_location
        bookings.p_date = bookings_p_date
        bookings.d_date = bookings_d_date
        bookings.p_up_time = bookings_p_up_time
        bookings.save()
        messages.success(request, 'Thank you for Contacting Us. One of our Agents will get to you in the next 24-48hrs')
        # return redirect(request, 'contact')
    else:
        bookings = Bookings()

    return render(request, 'home.html')

# Create your views here.
