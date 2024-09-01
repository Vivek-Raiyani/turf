from django.shortcuts import render
from .models import Facility
from teams.models import Sports

# Create your views here.
def login(request):
    if request.method == "POST":
        print("logged in")
        return render(request, 'templates/sports/home.html')  # Assuming this is the home page template
    return render(request, 'templates/sports/login.html')

def register(request):
    if request.method == "POST":
        print("registered")
        return render(request, 'templates/sports/login.html')
    return render(request, 'templates/sports/login.html')


def homepage(request):
          print("homepage")
          sports=Sports.objects.all()
          return render(request,'templates/sports/home.html',{'sports':sports})

def facilitylist(request, sport_name="yashi"):
          print("facilitylist")
          print(sport_name)
          sport=Sports.objects.get(sports=sport_name)
          print(sport)
          facilities = Facility.objects.filter(sports=sport)
          print(facilities)
          return render(request, 'templates/sports/facility_list.html', {'facilities': facilities,})


def facility_details(request, facility_id=1):
          print("facility_details")
          print(facility_id)
          facility=Facility.objects.get(id=facility_id)
          print(facility)
          return render(request, 'templates/sports/details.html', {'facility': facility,})

def sports_list(request):
          print("sports_list")
          sports=Sports.objects.all()
          print(sports[0].image)
          return render(request, 'templates/sports/sports_list.html', {'sports': sports})
          