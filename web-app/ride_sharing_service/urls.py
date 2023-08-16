from django.urls import path

from . import views

urlpatterns = [
    path('', views.overview_view, name='overview'),
    path('driver_edit_info', views.driver_edit_info_view, name='driver_edit_info'),
    path('request_ride', views.request_ride_view, name='request_ride'),
    path('owner_rides', views.owner_rides_view, name='rides'),
    path('owner_rides/<int:ride_id>/', views.owner_ride_detail_view, name='owner_ride_detail_view'),
    path('owner_rides/<int:ride_id>/edit', views.edit_owner_ride_detail_view, name='edit_owner_ride_detail_view'),
    path('driver_rides', views.driver_rides_view, name='driver_rides'),
    path('driver_rides/<int:ride_id>/', views.driver_ride_detail_view, name='driver_ride_detail_view'),
    path('sharer_search', views.sharer_search_view, name='sharer_search_view'),
    path('driver_search', views.driver_search_view, name='driver_search_view'),
    path('sharer_rides', views.sharer_rides_view, name='sharer_rides_view')
    ]