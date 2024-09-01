from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'sports'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.homepage, name='home'),
    path('sports/', views.sports_list, name='sports'),
    path('facility/<sport_name>/', views.facilitylist, name='facility'),
    path('details/<facility_id>/', views.facility_details, name='details'),
]


