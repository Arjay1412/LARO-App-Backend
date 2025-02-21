from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=25, verbose_name="First Name")
    lastname = models.CharField(max_length=25, verbose_name="Last Name")
    middlename = models.CharField(max_length=25, blank=True, null=True , verbose_name="Middle Name")
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=25)

    def __str__(self) -> str:
        return f"{self.lastname}, {self.firstname}"