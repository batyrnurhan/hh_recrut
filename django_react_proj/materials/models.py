from django.db import models
from rest_framework.authtoken.admin import User


# Create your models here.
class Material(models.Model):
    title = models.CharField("Title", max_length=50)
    description = models.CharField(max_length=150)
    document = models.CharField("Document", max_length=2000)
    cat = models.ForeignKey('CategoryOfMaterial', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class CategoryOfMaterial(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name