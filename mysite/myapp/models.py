from django.db import models

# Create your models here.

#creates a model for customers and new hires
class Person(models.Model):
    firstName = models.CharField(max_length = 20)
    lastName = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 80)
    Pword = models.CharField(max_length = 100)
    today = models.DateField(auto_now = True)
    
    def __str__(self):  #this is what will be seen in the database admin
        return self.firstName + ' ' + self.lastName