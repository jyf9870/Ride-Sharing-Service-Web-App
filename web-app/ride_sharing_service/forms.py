from django import forms

from .models import User
import datetime

VEHICLE_TYPES = (
    ('', ''),
    ('SUV', 'Sport Utility Vehicle'),
    ('Hatchback', 'Hatchback'),
    ('Crossover', 'Crossover'),
    ('Convertible', 'Convertible'),
    ('Sedan', 'Sedan'),
    ('Sports Car', 'Sports Car'),
    ('Coupe', 'Coupe'),
    ('Minivan', 'Minivan'),
    ('Truck', 'Pickup Truck'),
)
SHARED_CHOICES = [('True', 'Yes'), ('False', 'No')]


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "Password"}))


class UserSignupForm(forms.Form):
    username = forms.CharField(label="Username", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    # isDriver = forms.BooleanField(initial=False, required=False)


class DriverEditInfoForm(forms.Form):
    firstname = forms.CharField(label="First Name", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    lastname = forms.CharField(label="Last Name", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    vehicle_type = forms.ChoiceField(
        label="Vehicle Type", choices=VEHICLE_TYPES)
    plate_number = forms.CharField(label="License Plate Number", max_length=32,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    max_passengers = forms.IntegerField(label="Maximum Number of Passengers")
    special_vehicle_info = forms.CharField(
        label="Special Vehicle Information", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_driver = forms.BooleanField(label="Want to be a driver?", initial=False, required=False)


class RequestRideForm(forms.Form):
    destination = forms.CharField(label="Destination", max_length=512, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    arrival = forms.DateTimeField(
        label="Arrival Date", widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}))
  
    passenger_number = forms.IntegerField(label="Number of Passengers")
    is_shared = forms.ChoiceField(label="Share ride?", choices=SHARED_CHOICES)
    special_request = forms.CharField(label="Special Request (optional)", max_length=512,
                                      required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    requested_vehicle_type = forms.ChoiceField(
        label="Special Vehicle Type (optional)", initial=False, choices=VEHICLE_TYPES, required=False)


class SharerSearchForm(forms.Form):
    destination = forms.CharField(label="Destination", max_length=512, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    arrival_early = forms.DateTimeField(
        label="The Earliest Arrival Time", widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}))
    arrival_late = forms.DateTimeField(
        label="The latest Arrival Time", widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'})) 
    passenger_number = forms.IntegerField(label="Number of Passengers")

class DriverConfirmForm(forms.Form):
    ride_id = forms.CharField(label="RIDEID")

class SharerJoinForm(forms.Form):
    ride_id = forms.CharField(label="RIDEID")
    

class DriverEditRideForm(forms.Form):
    ride_id = forms.CharField(label="RIDEID")

class SharerQuitForm(forms.Form):
    ride_id = forms.CharField(label="RIDEID")