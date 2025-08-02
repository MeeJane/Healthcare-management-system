from django.db import models
from random import choices



#  Create your models here.


class Doctors(models.Model):
    class SpeType(models.TextChoices):
        Opthalmology='Opthalmology'
        Orthopedics='Orthopedics'
        Gastroenterology='Gastroenterology'
        Cardiology='Cardiology'
        Gynecology='Gynecology'
        ENT='ENT'
        Dentistry='Dentistry'
        Dermatology='Dermatology'
        Neurology='Neurology'
        General='General'
        Pediatrics='Pediatrics'
    Name = models.CharField(max_length=100)
    DID = models.IntegerField()
    Department=models.CharField(max_length=100,choices=SpeType.choices,default=SpeType.General)
    mobile_no=models.BigIntegerField()
    address=models.CharField(max_length=100)
    class Meta:
        db_table = "Doctors"

    def __str__(self):
        return self.Name


class Patients(models.Model):
    class GenType(models.TextChoices):
        male='male'
        female='female'
    class SpeType(models.TextChoices):
        Opthalmology='Opthalmology'
        Orthopedics='Orthopedics'
        Gastroenterology='Gastroenterology'
        Cardiology='Cardiology'
        Gynecology='Gynecology'
        ENT='ENT'
        Dentistry='Dentistry'
        Dermatology='Dermatology'
        Neurology='Neurology'
        General='General'
        Pediatrics='Pediatrics'
    Name=models.CharField(max_length=100)
    PID = models.IntegerField()
    Age = models.IntegerField()
    Gender = models.CharField(max_length=6,choices=GenType.choices,default=GenType.male)
    Department = models.CharField(max_length=100,choices=SpeType.choices,default=SpeType.General)
    appointment_date_time=models.DateTimeField()
    mobile_no = models.BigIntegerField()
    address = models.CharField(max_length=100)
    class Meta:
        db_table="Patients"

    def __str__(self):
        return self.Name
    

class Doc_Register(models.Model):
    
    
    
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=10)
    
    class Meta:
        db_table="Doc_Register"

class Adm_Register(models.Model):
    
    
    
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=10)
    
    class Meta:
        db_table="Adm_Register"


class Pat_Register(models.Model):
    
    
    
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=10)
    
    class Meta:
        db_table="Pat_Register"




