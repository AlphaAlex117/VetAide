from django import forms
from enum import Enum
from django.core.exceptions import ValidationError
import datetime

class OwnerForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    phone = forms.CharField(label='Phone', max_length=20)
    email = forms.EmailField(label='Email')
    addr = forms.CharField(label='Address', widget=forms.Textarea)

# Define the AnimalSize enum as before
class AnimalSize(Enum):
    Small = 'Small'
    Medium = 'Medium'
    Large = 'Large'

# Convert the AnimalSize enum into choices for a Django form field
ANIMAL_SIZE_CHOICES = [(size.name, size.value) for size in AnimalSize]

class PatientForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    owner_id = forms.CharField(label='Owner ID', max_length=100)
    medRecord_id = forms.CharField(label='Medical Record ID', max_length=100)
    animalType = forms.CharField(label='Animal Type', max_length=100)
    size = forms.ChoiceField(label='Size', choices=ANIMAL_SIZE_CHOICES)

class ScheduleForm(forms.Form):
    operation = forms.CharField(label='Operation', max_length=255)
    date = forms.DateField(label='Date', input_formats=['%m/%d/%Y'])

    def clean_date(self):
        date = self.cleaned_data['date']
        # Example of custom validation: ensure the date is not in the past
        if date < datetime.date.today():
            raise ValidationError("The date cannot be in the past.")
        return date

class MedicalRecordForm(forms.Form):
    vet_id = forms.CharField(label='Veterinarian ID', max_length=100)
    date = forms.DateField(label='Date', input_formats=['%m/%d/%Y'])
    reason = forms.CharField(label='Reason', widget=forms.Textarea)
    photo = forms.ImageField(label='Photo', required=False)  # Use ImageField for photo uploads

    def clean_date(self):
        date = self.cleaned_data['date']
        if date > datetime.date.today():
            raise ValidationError("The date cannot be in the future.")
        return date
    
class InventoryForm(forms.Form):
    generic_name = forms.CharField(label='Generic Name', max_length=255)
    brand_name = forms.CharField(label='Brand Name', max_length=255)
    amount = forms.FloatField(label='Amount')

class VeterinarianForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    userName = forms.CharField(label='Username', max_length=255)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class PhotoUploadForm(forms.Form):
    photo = forms.ImageField(label='Upload Photo')




