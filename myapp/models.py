from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.


class Hall(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    slot_7_10 = models.BooleanField(default=True)
    slot_10_1 = models.BooleanField(default=True)
    slot_1_4 = models.BooleanField(default=True)
    slot_4_7 = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Booking(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE)
    unit = models.CharField(max_length=100,default='')
    day = models.CharField(max_length=10, default='Monday')  # You might want to use DateField instead
    time_slot = models.CharField(max_length=20, default='7_10')  # You might want to use TimeField instead
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.lecturer.get_full_name()} - {self.unit} - {self.start_time} to {self.end_time}"
    
class BookingRequest(models.Model):
    lecturer = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    day = models.CharField(max_length=20)
    time_slot = models.CharField(max_length=20)
    
class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title