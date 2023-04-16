from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from urllib.parse import urlencode
from .forms import UserRegistrationForm, UserUpdateForm, RoomReservationForm
from .models import Rooms, Reservations
from datetime import date


def home(request):
    room=Rooms.objects.all()
    return render(request, 'hotelapp/home.html', {'room':room})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'hotelapp/register.html', context)

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

def roomInfo(request, room_id):
    room = Rooms.objects.get(pk=room_id)
    taken = False

    reserves = Reservations.objects.filter(room_ID = room_id)
    for re in reserves:
        if re.start_date < date.today() < re.end_date:
            taken = True
        elif re.end_date < date.today():
            re.delete()
            room.update(clean_status=0)
        else:
            taken = False

    if request.method in ('POST', 'PUT'):
        data = request.POST.copy()
        data['customer_ID'] = request.user.id
        data['room_ID'] = room_id
        data['room_name'] = room.name
        form = RoomReservationForm(data, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your reservation has been created. You can log in now!')
            return redirect('profile')
    else:
        form = RoomReservationForm()  
    
    context = {
        'user': request.user,
        'room': room,
        'form': form,
        'taken': taken,
    }
    
    return render(request, 'hotelapp/roomInfo.html', context)

@login_required
def profile(request):
    reserves = Reservations.objects.filter(customer_ID=request.user.id)
    rooms = Rooms.objects.all()
    
    context = {
        'user': request.user,
        'reserves': reserves,
        'rooms': rooms,
    }
    
    return render(request, 'hotelapp/profile.html', context)

def about(request):
	return render(request, 'hotelapp/about.html')

def components(request):
	return render(request, 'hotelapp/components.html')

def faq(request):
	return render(request, 'hotelapp/faq.html')

