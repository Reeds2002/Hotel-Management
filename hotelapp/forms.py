from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Reservations, Rooms


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

class RoomReservationForm(forms.ModelForm):
    customer_ID = forms.CharField(max_length=1000)
    room_ID = forms.CharField(max_length=3)
    start_date = forms.DateField()
    end_date = forms.DateField()
    room_name = forms.CharField(max_length=100)

    class Meta:
        model = Reservations
        fields = ['customer_ID', 'room_ID','start_date', 'end_date', 'room_name']

class RoomsUpdateForm(forms.ModelForm):
    status = forms.CharField()

    class Meta:
        model = Rooms
        fields = ['clean_status']
