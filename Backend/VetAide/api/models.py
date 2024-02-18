from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from pymongo import MongoClient
from datetime import datetime

# from typing import Optional
# from pydantic import BaseModel, Field
# from enum import Enum

# Create your models here.
# ORM: Object Relational Models

def setUpDatabase(clusterURL, dbName):
    client = MongoClient(clusterURL)
    db = client[dbName]
    print(f"Setup for database '{dbName}' is ready. Database will be created upon inserting the first document.")

def setUpCollection(clusterURL, dbName, collName):
    client = MongoClient(clusterURL)
    # Select the database
    db = client[dbName]
    # Prepare the collection object
    collection = db[collName]
    print(f"Setup for collection '{collName}' in database '{dbName}' is ready. The collection will be created upon inserting the first document.")

def initCollection(clusterURL, dbName, collName, doc):
    client = MongoClient(clusterURL)
    db = client[dbName]
    collection = db[collName]
    collection.insert_one(doc)
    print(f"Database '{dbName}' and collection '{collName}' created with the document inserted.")

def initOwner(clusterURL):
    doc = {
        'id': 0,
        'name': 'John Doe',
        'phone': '123-456-7890',
        'e-mail': 'john@doe.com',
        'address': 'baker street'
    }
    dbName = 'VetAide'
    collName = 'Owner'
    initCollection(clusterURL,dbName,collName, doc)

def initPatient(clusterURL):
    doc = {
        'id': 0,
        'owner_id': 0,
        'name': 'john doe',
        'med_history_id': 0,
        'category_name': 'MAN',
        'cateory_size': 'FAT'
    }
    dbName = 'VetAide'
    collName = 'Patient'
    initCollection(clusterURL,dbName,collName, doc)

def initSchedule(clusterURL):
    doc = {
        'id': 0,
        'operation_category': 'SEX',
        'date': datetime.strptime('2024-02-18 04:46:51.507162', '%m/%d/%y %H:%M:%S'),
        'patient':'john doe',
        'veterinary': 'your mom',
        'owner': 'John Doe'
    }
    dbName = 'VetAide'
    collName = 'Schedule'
    initCollection(clusterURL,dbName,collName,doc)

def initMedHistory(clusterURL):
    doc={
        'id': 0,
        'veterinary_id': 0,
        'date': datetime.strptime('2024-02-18 04:46:51.507162', '%m/%d/%y %H:%M:%S'),
        'patient': 'john doe',
        'reason': 'GAY',
        'photo': ''
        }
    dbName= 'VetAide'
    collName ='Medical History'
    initCollection(clusterURL,dbName,collName,doc)

def initInventory(clusterURL):
    doc = {
        'id': 0,
        'generic_name': 'Viagra',
        'brand_name': 'Ricola',
        'amount' : 1000000.0
    }
    dbName = 'VetAide'
    collName = 'Inventory'
    initCollection(clusterURL,dbName, collName, doc)

def initPhotos(clusterURL):
    doc = {
        'id': 0,
        'url':''
    }
    dbName = 'VetAide'
    collName = 'Photos'
    initCollection(clusterURL,dbName,collName,doc)

def initVeterinarian(clusterURL):
    doc = {
        'id':0,
        'name':'jane doe',
        'username':'admin',
        'password':'password'
    }
    dbName = 'VetAide'
    collName = 'Veterinarian'
    initCollection(clusterURL,dbName,collName,doc)

class Owner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    eMail = models.EmailField()
    addr = models.TextField()

    def __str__(self):
        return self.name

class AnimalSize(models.TextChoices):
    SMALL = 'Small', _('Small')
    MEDIUM = 'Medium', _('Medium')
    LARGE = 'Large', _('Large')

class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    owner_id = models.CharField(max_length=255)
    medRecord_id = models.CharField(max_length=255)
    AnimalType = models.CharField(max_length=255)
    Size = models.CharField(
        max_length=50,
        choices=AnimalSize.choices,
        default=AnimalSize.SMALL,
    )

    def __str__(self):
        return self.name

class Schedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operation = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f"{self.operation} on {self.date}"

class MedicalRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vet_id = models.CharField(max_length=255)
    date = models.DateField()
    reason = models.TextField()
    photo = models.ImageField(upload_to='medical_records_photos/')

    def __str__(self):
        return f"Medical Record for {self.reason} on {self.date}"

class Inventory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    generic_name = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255)
    amount = models.FloatField()

    def __str__(self):
        return f"{self.generic_name} ({self.brand_name}) - {self.amount}"

class Veterinarian(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    userName = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    
# class Owner(BaseModel):
#     id: str = Field(default_factory=uuid.uuid4, alias="_id")
#     name: str = Field(...)
#     phone: str = Field(...)
#     eMail: str = Field(...)
#     addr: str = Field(...)

#     class Config:
#         allow_population_by_field_name = True
#         schema_extra = {
#             "example": {
#                 "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
#                 "name": "Don Quixote",
#                 "phone": "(212)345-6789",
#                 "eMail": "...",
#                 "addr": "..."
#             }
#         }

# class AnimalSize(Enum):
#     Small = 'Small'
#     Medium = 'Medium'
#     Large = 'Large'

# class Patient(BaseModel):
#     id: str = Field(default_factory=uuid.uuid4, alias="_id")
#     name: str = Field(...)
#     owner_id: str = Field(...)
#     medRecord_id: str = Field(...)
#     AnimalType: str = Field(...)
#     Size: AnimalSize

#     class Config:
#         allow_population_by_field_name = True
#         schema_extra = {
#             "example": {
#                 "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
#                 "name": "Don Quixote",
#                 "owner_id": "(212)345-6789",
#                 "medRecord_id": "...",
#                 "AnimalType": "...",
#                 "Size": "..."
#             }
#         }

# class Schedule(BaseModel):
#     id: str = Field(default_factory=uuid.uuid4, alias="_id")
#     operation: str = Field(...)
#     date: str = Field(...)

#     class Config:
#         allow_population_by_field_name = True
#         schema_extra = {
#             "example": {
#                 "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
#                 "operation": "Surgery",
#                 "date": "09/11/2001"
#             }
#         }

# class MedicalRecord(BaseModel):
#     id: str = Field(default_factory=uuid.uuid4, alias="_id")
#     vet_id: str = Field(...)
#     date: str = Field(...)
#     reason: str = Field(...)
#     photo: str = Field(...)

#     class Config:
#         allow_population_by_field_name = True
#         schema_extra = {
#             "example": {
#                 "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
#                 "vet_id": "...",
#                 "date": "",
#                 "reason": "...",
#                 "photo": "..."
#             }
#         }

# class Inventory(BaseModel):
#     id: str = Field(default_factory=uuid.uuid4, alias="_id")
#     generic_name: str = Field(...)
#     brand_name: str = Field(...)
#     amount: float = Field(...)

#     class Config:
#         allow_population_by_field_name = True
#         schema_extra = {
#             "example": {
#                 "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
#                 "generic_name": "Don Quixote",
#                 "brand_name": "(212)345-6789",
#                 "amount": "..."
#             }
#         }

# class Veterinarian(BaseModel):
#     id: str = Field(default_factory=uuid.uuid4, alias="_id")
#     name: str = Field(...)
#     userName: str = Field(...)
#     password: str = Field(...)

#     class Config:
#         allow_population_by_field_name = True
#         schema_extra = {
#             "example": {
#                 "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
#                 "name": "Don Quixote",
#                 "userName": "admin",
#                 "password": "password"
#             }
#         }
# class Photos(BaseModel):
#     id: str = Field(...)
#     url: str = Field(...)

#     class Config: 
#         allow_population_by_field_name = True
#         schema_extra = {
#             "example": {
#                 "_id": "...",
#                 "url": "..."
#             }
#         }
# ---------------------------------------------------