from django.urls import path

from . import views

# urls related to booking, cancled and payment
urlpatterns = [
          path('', views.history, name='history'),
]