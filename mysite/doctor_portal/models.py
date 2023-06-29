from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    '''A patient with all their info'''
    def __str__(self) -> str:
        return self.last_name + ', ' + self.first_name
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    birthdate = models.DateTimeField("Birthdate")


class Diagnosis(models.Model):
    '''Different diagnoses or types of cancer'''
    description = models.CharField(max_length=100)


class Plan(models.Model):
    '''A patient's treatment plan, including several treatments.'''
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    number_of_treatments = models.SmallIntegerField("Treatments")
    total_dose = models.SmallIntegerField("Total dose")


class Treatment(models.Model):
    '''includes one radiation treatment on a patient.'''
    pass

