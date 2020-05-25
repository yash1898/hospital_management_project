from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class Doctor(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    special=models.CharField(max_length=50)
    salary=models.IntegerField(default=0)
    def __str__ (self):
        return self.name

class Patient(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.IntegerField()
    address=models.CharField(max_length=150)
    symptoms=models.CharField(default='none',max_length=150)
    age=models.IntegerField(default=0)
    fees=models.CharField(max_length=30,default='Unpaid')
    def __str__ (self):
        return self.name

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date1=models.DateField()
    time1=models.TimeField()
    

    def __str__(self):
        return self.doctor.name+"--"+self.patient.name

class Register_Patient(models.Model):
    username=models.CharField(max_length=50)
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)

    def __str__ (self):
        return self.username

class Register(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    is_doctor=models.CharField(max_length=100)

    def __str__(self):
        return self.username.username+"--"+ self.is_doctor