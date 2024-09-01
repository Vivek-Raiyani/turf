from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sponsers(models.Model):
          name = models.CharField(max_length=100)
          image = models.ImageField()
          description = models.TextField()
          amount = models.IntegerField()

          def __str__(self):
                    return self.name

class Tournament(models.Model):
          name = models.CharField(max_length=100,null=True)
          date = models.DateField(null=True)
          time = models.TimeField(null=True)
          sport_type = models.CharField(max_length=100,null=True)
          venue = models.CharField(max_length=100,null=True)
          winner = models.CharField(max_length=100,null=True)
          runner_up = models.CharField(max_length=100,null=True)
          third_place = models.CharField(max_length=100,null=True)
          participant = models.IntegerField(null=True)
          prize_pool = models.IntegerField(null=True)
          sponsers=models.ManyToManyField(Sponsers)

          def __str__(self):
                    return self.name

class TournamnetTeams(models.Model):
          team_name=models.CharField(max_length=20,null=True)
          member=models.ManyToManyField(User)
          
          def __str__(self):
                    return self.team_name
    
class participants(models.Model):
          tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE)
          user = models.ForeignKey(User,on_delete=models.CASCADE)
          team = models.ForeignKey(TournamnetTeams,on_delete=models.CASCADE,null=True)
          payment = models.BooleanField(default=False)
          payment_id = models.CharField(max_length=100,null=True)
          
          def __str__(self):
                    return str(self.user)