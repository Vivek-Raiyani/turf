from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
CREATE TABLE Teams (
    TeamID INT PRIMARY KEY AUTO_INCREMENT,
    TeamName VARCHAR(100),
    CoachID INT,
    SportType VARCHAR(50),
    DateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CoachID) REFERENCES Users(UserID)
);

CREATE TABLE Players (
    PlayerID INT PRIMARY KEY AUTO_INCREMENT,
    UserID INT,
    TeamID INT,
    Position VARCHAR(50),
    JerseyNumber INT,
    Height DECIMAL(5,2),
    Weight DECIMAL(5,2),
    SkillLevel VARCHAR(50),
    DateJoined DATE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID)
);
'''

class Sports(models.Model):
          sports=models.CharField(max_length=30,null=True)
          sports_type=models.CharField(choices=(
                    ("indoor","Indoor"),
                    ("outdoor","Outdoor"),
                    ("both","Both")
          ),null=True,max_length=10)
          image=models.ImageField(upload_to="sports",null=True)
          
          def __str__(self):
            return self.sports

class Teams(models.Model):
    team_name=models.CharField(max_length=20,null=True)
    coach=models.ManyToManyField(User)
    sport_type=models.ForeignKey(Sports,on_delete=models.CASCADE)
    register_date=models.DateField(auto_created=True)

    def __str__(self):
        return self.team_name

class Players(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    team=models.ForeignKey(Teams,on_delete=models.CASCADE)
    position=models.CharField(max_length=50,null=True)
    jersey_number=models.IntegerField(null=True)
    height=models.DecimalField(max_digits=5,decimal_places=2,null=True)
    weight=models.DecimalField(max_digits=5,decimal_places=2,null=True)
    skill_level=models.CharField(max_length=50,null=True)
    date_joined=models.DateField(auto_created=True)
    
    def __str__(self):
        return self.user