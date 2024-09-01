from django.db import models
from facilities.models import Facility
from django.contrib.auth.models import User
# Create your models here.
'''
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,
    FacilityID INT,
    UserID INT,
    StartTime DATETIME,
    EndTime DATETIME,
    BookingStatus ENUM('Confirmed', 'Pending', 'Cancelled'),
    Purpose VARCHAR(100),
    DateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (FacilityID) REFERENCES Facilities(FacilityID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
'''

class Slot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def __str__(self):
        return str(self.start_time)

class Booking(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_status = models.BooleanField(default=False)
    purpose = models.CharField(max_length=30, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    booking_slot=models.ManyToManyField(Slot)
    cancelled = models.BooleanField(default=False)
    reason=models.CharField(max_length=100, blank=True, null=True)
    payment=models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.facility)