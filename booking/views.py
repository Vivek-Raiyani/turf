from django.shortcuts import render

# Create your views here.
def history(request):
          bokking=[1,2,3,4,5]
          return render(request,'templates/sports/history.html',{'bookings':bokking})