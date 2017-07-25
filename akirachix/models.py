from django.db import models
import datetime

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length = 100)
    course = models.CharField(max_length = 50) 
    description = models.TextField(default = 'Good student')
    registration_date = models.DateField(default = datetime.date(2017,1,1))
    graduation_date = models.DateField(default = datetime.date(2017,1,1))

class Teachers(models.Model):
    name = models.CharField(max_length = 100)
    course = models.CharField(max_length = 50) 
    description = models.TextField(default = 'Python Guru')
    availability_date = models.DateField(default = datetime.date(2017,1,1))
    
class Courses(models.Model):
    title = models.CharField(max_length = 100)
    course = models.CharField(max_length = 50) 
    trainer = models.TextField(default = 'Yoga trainer')
    location = models.TextField(default = 'Bishop Magua')
    
    

    
    
    
          