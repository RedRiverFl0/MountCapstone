from django.db import models

# Create your models here.

#creates a model for customers and new hires
class Person(models.Model):
    firstName = models.CharField(max_length = 20)
    lastName = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 80)
    phone = models.CharField(max_length = 25)
    file = models.FileField(upload_to= 'tasks/')
    today = models.DateField(auto_now = True)
    
    def __str__(self):  #this is what will be seen in the database admin
        return self.firstName + ' ' + self.lastName
    
class Hire(models.Model):
    firstName = models.CharField(max_length = 20)
    lastName = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 80)
    phone = models.CharField(max_length = 25)
    file = models.FileField(upload_to='resumes/')
    today = models.DateField(auto_now = True)

    def __str__(self):  #this is what will be seen in the database admin
        return self.firstName + ' ' + self.lastName
    

