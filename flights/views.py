from django.shortcuts import *
from django.http import *
from django.urls import reverse
from .models import * # importing table
# Create your views here.
def index(request):
    return render(request,"flights/index.html",{
    "flights":Flight.objects.all()  #select * from Flight
    })

# for information of selected flight
def flight(request,flight_id):
    flight=Flight.objects.get(pk=flight_id)  #pk-->primary key

    return render(request,"flights/flight.html",{
    "flight":flight,
    "passengers":flight.passengers.all(),  #here passengers is relation
    "non_passengers":Passenger.objects.exclude(flights=flight).all()
    })


def book(request,flight_id):
    if request.method=="POST":
        flight=Flight.objects.get(pk=flight_id)
        passenger=Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)  #add new passenger in flight
        # take that passenger
        #from given set of flights
        #add add passenger to that Flight
        return HttpResponseRedirect(reverse("flight",args=(flight.id,))) #last comma is imp
