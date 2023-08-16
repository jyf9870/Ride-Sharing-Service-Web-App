from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages

from django.http import HttpResponse
from .forms import UserSignupForm, UserLoginForm, DriverEditInfoForm
from .forms import RequestRideForm, SharerSearchForm, DriverEditRideForm, DriverConfirmForm,SharerJoinForm,SharerQuitForm
from .models import User, Ride, Sharer
from django.core.mail import send_mail
from hw1 import settings


def welcome_view(request, *arg, **kwargs):
    return render(request, "welcome.html", {})


def signup_view(request, *arg, **kwargs):
    form = UserSignupForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        user = User()
        user.username = username
        user.password = password
        user.email = email
        user.save()
        return redirect('/login')
    context = {'form': form}
    return render(request, "signup.html", context)


def login_view(request, *arg, **kwargs):
    form = UserLoginForm(request.POST or None)
    error_msg = ""

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            error_msg = "Invalid user."
            context = {'form': form, 'error_msg': error_msg}
            return render(request, "login.html", context)
        if password == user.password:
            request.session['authenticated'] = True
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['is_driver'] = user.is_driver
            return redirect('/overview')
        else:
            error_msg = "Invalid username or password."
            context = {'form': form, 'error_msg': error_msg}
            return render(request, "login.html", context)
    context = {'form': form, 'error_msg': error_msg}
    return render(request, "login.html", context)


def overview_view(request, *arg, **kwargs):
    return render(request, "overview.html", {})


def logout_view(request, *arg, **kwargs):
    request.session.flush()
    return redirect("/")


def driver_edit_info_view(request, *arg, **kwargs):
    user_id = request.session.get('user_id')
    user = get_object_or_404(User, pk=user_id)
    # user already has some previous info
    initial = {}
    if user.is_driver:
        initial['firstname'] = user.firstname
        initial['lastname'] = user.lastname
        initial['vehicle_type'] = user.vehicle_type
        initial['plate_number'] = user.plate_number
        initial['max_passengers'] = user.max_passengers
        initial['special_vehicle_info'] = user.special_vehicle_info
        initial['is_driver'] = user.is_driver
    form = DriverEditInfoForm(request.POST or None, initial=initial)
    error_msg = ""
    if form.is_valid():
        # obtain data from form
        firstname = form.cleaned_data.get('firstname')
        lastname = form.cleaned_data.get('lastname')
        vehicle_type = form.cleaned_data.get('vehicle_type')
        plate_number = form.cleaned_data.get('plate_number')
        max_passengers = form.cleaned_data.get('max_passengers')
        special_vehicle_info = form.cleaned_data.get('special_vehicle_info')
        is_driver = form.cleaned_data.get('is_driver')
        # some error handling
        if not is_driver and not user.is_driver:
            error_msg = "You must click the checkbox to confirm to be a driver."
            context = {'form': form, 'error_msg': error_msg}
            return render(request, "driver_edit_info.html", context)
        if max_passengers < 1 or max_passengers > 50:
            error_msg = "Please enter a number of passengers between 1 and 50."
            context = {'form': form, 'error_msg': error_msg}
            return render(request, "driver_edit_info.html", context)
        # save the user info
        user.firstname = firstname
        user.lastname = lastname
        user.vehicle_type = vehicle_type
        user.plate_number = plate_number
        user.max_passengers = max_passengers
        user.special_vehicle_info = special_vehicle_info
        user.is_driver = is_driver
        # update driver status in user session
        request.session['is_driver'] = user.is_driver
        user.save()
        context = {'form': form, 'error_msg': error_msg}
        return redirect("/overview")
    context = {'form': form, 'error_msg': error_msg}
    return render(request, 'driver_edit_info.html', context)


def request_ride_view(request, *arg, **kwargs):
    user_id = request.session.get('user_id')
    user = get_object_or_404(User, pk=user_id)
    form = RequestRideForm(request.POST or None)
    error_msg = ""
    if form.is_valid():
        destination = form.cleaned_data.get('destination')
        arrival = form.cleaned_data.get('arrival')
        passenger_number = form.cleaned_data.get('passenger_number')
        is_shared = form.cleaned_data.get('is_shared')
        special_request = form.cleaned_data.get('special_request')
        requested_vehicle_type = form.cleaned_data.get(
            'requested_vehicle_type')
        # some error handling
        if passenger_number < 1 or passenger_number > 50:
            error_msg = "Please enter a number of passengers between 1 and 50."
            context = {'form': form, 'error_msg': error_msg}
            return render(request, "request_ride.html", context)
        # create the new ride
        new_ride = Ride()
        new_ride.owner = user
        new_ride.destination = destination
        new_ride.arrival = arrival
        new_ride.passenger_number = passenger_number
        new_ride.is_shared = is_shared
        new_ride.special_request = special_request
        new_ride.requested_vehicle_type = requested_vehicle_type
        new_ride.save()
        all_rides = Ride.objects.all()
        context = {'form': form, 'error_msg': error_msg,
                   'all_rides': all_rides}
        return render(request, "overview.html", context)
    context = {'form': form, 'error_msg': error_msg}
    return render(request, "request_ride.html", context)


def owner_rides_view(request, *arg, **kwargs):
    user_id = request.session.get('user_id')
    owner_rides = Ride.objects.filter(owner=user_id)
    sharer_rides = Ride.objects.filter(sharer=user_id)
    context = {
        'owner_rides': owner_rides,
        'sharer_rides': sharer_rides
    }
    return render(request, "owner_rides.html", context)

def sharer_rides_view(request, *arg, **kwargs):
    user_id = request.session.get('user_id')
    user = get_object_or_404(User, pk=user_id)
    sharer_rides = Ride.objects.filter(sharer=user)
    form = SharerQuitForm(request.POST or None)
    if form.is_valid():
        ride_id = form.cleaned_data.get("ride_id")
        ride = get_object_or_404(Ride, pk=ride_id)
        sharers = Sharer.objects.filter(user = user, ride = ride, joined = True)
        for share in sharers:
            ride.passenger_number -= share.passenger_number
            share.joined = False
            share.save()
        
        ride.sharer.remove(user)
        ride.save()
        context = {
            'sharer_rides': sharer_rides,
            'form': form,
        }
        return render(request, "sharer_rides.html", context)
    context = {
        'sharer_rides': sharer_rides,
        'form': form
    }
    return render(request, "sharer_rides.html", context)


def driver_rides_view(request, *arg, **kwargs):
    user_id = request.session.get('user_id')
    driver_rides = Ride.objects.filter(driver=user_id)
    form = DriverConfirmForm(request.POST or None)
    if form.is_valid():
        ride_id = form.cleaned_data.get("ride_id")
        ride = get_object_or_404(Ride, pk=ride_id)
        ride.status = "Completed"
        ride.save() 
        return redirect('/overview/driver_rides')
    context = {'driver_rides': driver_rides, 'form': form}
    return render(request, "driver_rides.html", context)


def owner_ride_detail_view(request, ride_id, *arg, **kwargs):
    user_id = request.session.get('user_id')
    user = get_object_or_404(User, pk=user_id)
    ride = get_object_or_404(Ride, pk=ride_id)
    context = {'user': user, 'ride': ride}
    return render(request, "ride_detail.html", context)

def sharer_search_view(request, *arg, **kwargs):
    user_id = request.session.get('user_id')
    user = get_object_or_404(User, pk=user_id)
    form = SharerSearchForm(request.POST or None)
    formJoin = SharerJoinForm(request.POST or None)
    error_msg = ""
    if form.is_valid():
        destination = form.cleaned_data.get('destination')
        arrival_early = form.cleaned_data.get('arrival_early')
        arrival_late = form.cleaned_data.get('arrival_late')

        sharer_search_temp = Ride.objects.filter(destination=destination, arrival__gte=arrival_early,
                                            arrival__lte=arrival_late,
                                            is_shared=True, status="Open")
        sharer_search = set()
        for ride in sharer_search_temp:
            if not ride.sharer.all().contains(user):
                sharer_search.add(ride)
        search_size = len(sharer_search)

        temp_sharer_passenger_num = form.cleaned_data.get('passenger_number')
        # some error handling
        if temp_sharer_passenger_num < 1 or temp_sharer_passenger_num > 50:
            error_msg = "Please enter a number of passengers between 1 and 50."
            context = {'form': form, 'error_msg': error_msg}
            return render(request, "sharer_search.html", context)
        
        user.temp_sharer_passenger_num = temp_sharer_passenger_num
        user.save()
        context = {'form': form, 'error_msg': error_msg,'sharer_search': sharer_search,
                    'user': user, 'search_size': search_size, 'temp_sharer_passenger_num':temp_sharer_passenger_num
                    }
        return render(request, "sharer_search.html", context)
    
    if formJoin.is_valid():
        ride_id = formJoin.cleaned_data.get("ride_id")
        ride = get_object_or_404(Ride, pk=ride_id)
        user = get_object_or_404(User, pk=user_id)
         # create the new sharer ride
        new_sharer = Sharer()
        new_sharer.passenger_number = user.temp_sharer_passenger_num
        new_sharer.ride = ride
        new_sharer.user = user
        new_sharer.joined = True
        new_sharer.save()
        ride.passenger_number += user.temp_sharer_passenger_num
        ride.sharer.add(user)
        ride.save()
        context = {
            'formJoin': formJoin
        }
        return redirect('/overview/sharer_rides')
    context = {'form': form,'error_msg': error_msg}
    return render(request, "sharer_search.html", context)


def driver_search_view(request, *arg, **kwargs):
    user_id = request.session.get('user_id')
    user = get_object_or_404(User, pk=user_id)
    driver_search = Ride.objects.filter(requested_vehicle_type = user.vehicle_type,
                                        passenger_number__lte=user.max_passengers,
                                        special_request=user.special_vehicle_info, status="Open")
    driver_search|= Ride.objects.filter(requested_vehicle_type = "",
                                    passenger_number__lte=user.max_passengers,
                                    special_request=user.special_vehicle_info, status="Open")
        
    form = DriverConfirmForm(request.POST or None)
    if form.is_valid():
        ride_id = form.cleaned_data.get("ride_id")
        ride = get_object_or_404(Ride, pk=ride_id)
        ride.status = "Confirmed"          
        ride.driver = user
        ride.save()
        # send email to owner and all sharers
        email_title_owner = f'{ride.owner}, your ride has been confirmed!'
        email_body_owner = f'You ride id is {ride.id}. Your driver is {ride.driver}. You are going to {ride.destination} with an arrival time of {ride.arrival}.'
        email_owner = ride.owner.email
        send_mail(email_title_owner, email_body_owner, settings.EMAIL_FROM, [email_owner])
        for sharer in ride.sharer.all():
            email_title_sharer = f'{sharer.username}, your shared ride has been confirmed!'
            email_body_sharer = f'Your ride id is {ride.id}. This ride is owned by {ride.owner} and driven by {ride.driver}. You are going to {ride.destination} with an arrival time of {ride.arrival}.'
            email_sharer = sharer.email
            send_mail(email_title_sharer, email_body_sharer, settings.EMAIL_FROM, [email_sharer])
        driver_search = Ride.objects.filter(requested_vehicle_type=user.vehicle_type,
                                        passenger_number__lte=user.max_passengers,
                                        special_request=user.special_vehicle_info, status="Open")
        driver_search|= Ride.objects.filter(requested_vehicle_type = "",
                                    passenger_number__lte=user.max_passengers,
                                    special_request=user.special_vehicle_info, status="Open")
        context = {'user': user, 'driver_search': driver_search, 'form': form}
        return render(request, "driver_search.html", context)
    context = {'user': user, 'driver_search': driver_search, 'form': form}
    return render(request, "driver_search.html", context)
        
def edit_owner_ride_detail_view(request, ride_id, *arg, **kwargs):
    user_id = request.session.get('user_id')
    user = get_object_or_404(User, pk=user_id)
    ride = get_object_or_404(Ride, pk=ride_id)
    initial = {}
    initial['destination'] = ride.destination
    initial['arrival'] = ride.arrival
    initial['passenger_number'] = ride.passenger_number
    initial['is_shared'] = ride.is_shared
    initial['special_request'] = ride.special_request
    initial['requested_vehicle_type'] = ride.requested_vehicle_type
    form = RequestRideForm(request.POST or None, initial=initial)
    error_msg = ""

    if form.is_valid():
        destination = form.cleaned_data.get('destination')
        arrival = form.cleaned_data.get('arrival')
        passenger_number = form.cleaned_data.get('passenger_number')
        is_shared = form.cleaned_data.get('is_shared')
        special_request = form.cleaned_data.get('special_request')
        requested_vehicle_type = form.cleaned_data.get(
            'requested_vehicle_type')
        # some error handling
        if passenger_number < 1 or passenger_number > 50:
            error_msg = "Please enter a number of passengers between 1 and 50."
            context = {'form': form, 'error_msg': error_msg}
            return render(request, "edit_owner_ride.html", context)
        # create the new ride
        ride.destination = destination
        ride.arrival = arrival
        ride.passenger_number = passenger_number
        ride.is_shared = is_shared
        ride.special_request = special_request
        ride.requested_vehicle_type = requested_vehicle_type
        ride.save()
        return redirect('/overview/owner_rides')
    context = {'form': form, 'error_msg': error_msg}
    return render(request, "edit_owner_ride.html", context)


def driver_ride_detail_view(request, ride_id, *arg, **kwargs):
    user_id = request.session.get('user_id')
    user = get_object_or_404(User, pk=user_id)
    ride = get_object_or_404(Ride, pk=ride_id)
    context = {'user': user, 'ride': ride}
    return render(request, "ride_detail.html", context)