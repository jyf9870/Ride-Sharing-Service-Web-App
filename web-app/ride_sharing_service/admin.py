from django.contrib import admin

from .models import User, Ride, Sharer

admin.site.register(User)
admin.site.register(Ride)
admin.site.register(Sharer)
