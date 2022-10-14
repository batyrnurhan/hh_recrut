from enum import unique
from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField("Name", max_length=50)
    surname = models.CharField("Surnanme",default='null', max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    document = models.CharField("Document", max_length=200)
    is_staff = models.BooleanField(default =False)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name