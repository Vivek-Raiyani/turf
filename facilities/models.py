from django.db import models
from django.contrib.auth.models import User
from teams.models import Sports
# Create your models here.
'''
CREATE TABLE Facilities (
    FacilityID INT PRIMARY KEY AUTO_INCREMENT,
    FacilityName VARCHAR(100),
    FacilityType ENUM('Court', 'Field', 'Gym', 'Pool'),
    Location VARCHAR(255),
    Capacity INT,
    OperatingHours VARCHAR(50),
    ManagerID INT,
    DateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ManagerID) REFERENCES Users(UserID)
);
'''
class FacilityType(models.Model):
          facility_type=models.CharField(choices=[('Court','Court'),('Field','Field'),('Gym','Gym'),('Pool','Pool'),('Other','Other')],null=True,max_length=20)

          def __str__(self):
                    return self.facility_type

class FacilityLocation(models.Model):
          facility_address=models.CharField(max_length=100,null=True)
          city=models.CharField(max_length=30,null=True)
          state=models.CharField(max_length=20,null=True)
          
          def __str__(self):
                    return self.city
          

class Facility(models.Model):
          name=models.CharField(max_length=100,null=True)
          sports=models.ForeignKey(Sports,on_delete=models.CASCADE)
          type=models.ForeignKey(FacilityType,on_delete=models.CASCADE)
          location=models.ForeignKey(FacilityLocation,on_delete=models.CASCADE)
          capacity=models.IntegerField(null=True)
          manager=models.ForeignKey(User,on_delete=models.CASCADE)
          register_date=models.DateTimeField(auto_now_add=True)
          image1=models.ImageField(blank=True,null=True)
          image2=models.ImageField(blank=True,null=True)
          image3=models.ImageField(blank=True,null=True)
          video=models.FileField(blank=True,null=True)
          available=models.BooleanField(default=True)
          
          def __str__(self):
                    return self.name
                
class Review(models.Model):
          user=models.ForeignKey(User,on_delete=models.CASCADE)
          facility=models.ForeignKey(Facility,on_delete=models.CASCADE)
          rating=models.IntegerField(null=True)
          comment=models.CharField(max_length=100,null=True)
          date_created=models.DateTimeField(auto_now_add=True)
          
          def __str__(self):
                    return str(self.user)