from django.db import models

VEHICLE_TYPES = {
    ('SUV', 'Sport Utility Vehicle'),
    ('Hatchback', 'Hatchback'),
    ('Crossover', 'Crossover'),
    ('Convertible', 'Convertible'),
    ('Sedan', 'Sedan'),
    ('Sports Car', 'Sports Car'),
    ('Coupe', 'Coupe'),
    ('Minivan', 'Minivan'),
    ('Truck', 'Pickup Truck'),
}

# a ride can be 1. open 2. confirmed 3. complete
STATUS_CHOICES= {
    ('Open','Open'),
    ('Confirmed','Confirmed'),
    ('Completed', 'Completed')
}

class User(models.Model):
    # info when signing up #
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    
    # info when registering as driver: personal info
    is_driver = models.BooleanField(default=False, null=True, blank=True)
    firstname = models.CharField(max_length=128, null=True, blank=True)
    lastname = models.CharField(max_length=128, null=True, blank=True)
    # info when registering as driver: vehicle info
    
    vehicle_type = models.CharField(max_length=64, choices=VEHICLE_TYPES, null=True, blank=True)
    plate_number = models.CharField(max_length=32, null=True, blank=True)
    max_passengers = models.IntegerField(null=True, blank=True)
    special_vehicle_info = models.CharField(max_length=1024, null=True, blank=True)

    #temperary passenger number storage
    temp_sharer_passenger_num = models.IntegerField(null=True, blank=True)

    
    def __str__(self):
        return self.username


class Ride(models.Model):
    # users
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='owner')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='driver')
    sharer = models.ManyToManyField(User, related_name="sharer", blank=True)
    # ride info
    destination = models.CharField(max_length=512)
    arrival = models.DateTimeField(blank=True, null=True)
    passenger_number = models.IntegerField()
    current_passenger_number = models.IntegerField(blank=True, null=True)
    is_shared = models.BooleanField(default=False)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default="Open")
    # optional fields
    special_request = models.CharField(default="", max_length=512, blank=True, null=True)
    requested_vehicle_type = models.CharField(default="", max_length=64, choices=VEHICLE_TYPES, null=True, blank=True)
    
    def __str__(self):
        return f'Going to {self.destination}...'
    

class Sharer(models.Model):
    passenger_number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='user')
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, blank=True, null=True, related_name='ride')
    joined = models.BooleanField(default=False)

    def __str__(self):
        return self.passenger_number
