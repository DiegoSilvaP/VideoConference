# usuario/models.py
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models




class User(AbstractUser):
    is_medical = models.BooleanField(default=False)
    # is_physiotherapist = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

    class Meta:
        db_table = 'auth_user'


class MedicalProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)


# class PhysiotherapistProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     active = models.BooleanField(default=True)
#     name = models.CharField(max_length=64)