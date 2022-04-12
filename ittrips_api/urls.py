from django.urls import path
from . import views

urlpatterns = [
    path('api/trips', views.TripList.as_view(), name='Trip_list'), # api/Trips will be routed to the TripList view for handling
    path('api/trips/<int:pk>', views.TripDetail.as_view(), name='Trip_detail'), # api/Trips will be routed to the TripDetail view for handling
]