from django.db import models

# Create your models here.
class Patient(models.Model):
    '''A patient with all their info'''
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    birthdate = models.DateTimeField("Birthdate")

class Plan(models.Model):
    '''A patient's treatment plan, including several treatments.'''
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.CharField()
    number_of_treatments = models.SmallIntegerField("Treatments")
    total_dose = models.SmallIntegerField("Total dose")

class Treatment(models.Model):
    '''includes one radiation treatment on a patient.'''
    pass

class Diagnosis(models.Model):
    '''Different diagnoses or types of cancer'''
    pass