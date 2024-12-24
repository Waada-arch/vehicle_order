from django.db import models

# Create your models here.
class login(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    age=models.IntegerField()
    message=models.TextField()
    gender=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class driver(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    aadhaar = models.IntegerField()
    license = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    vehicle = models.CharField(max_length=50)
    availability = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"