
from django.db import models
from django_countries.fields import CountryField

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Department(models.Model):
    country = models.ForeignKey(Country,on_delete=models.SET_NULL,
        null=True, verbose_name=('Country'))
    name = models.CharField(max_length=100)

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL,
        null=True, verbose_name=('Country'))
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,
        null=True,
        verbose_name=("Department"))

class Registry (models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    #country = CountryField(blank_label='(select country)')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL,
        null=True, verbose_name=('Country'))
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,
        null=True, verbose_name=("Department"))

    