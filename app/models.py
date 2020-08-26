from django.db import models
from smart_selects.db_fields import ChainedForeignKey

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Department(models.Model):
    country = models.ForeignKey(Country,on_delete=models.SET_NULL,
        null=True, verbose_name=('Country'))
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL,
        null=True, verbose_name=('Country'))
    department = ChainedForeignKey(
        Department, 
        chained_field="country",
        chained_model_field="country", 
        show_all=False, 
        auto_choose=True,
        default ="",
        blank=True
    )
    def __str__(self):
        return self.name

class Registry (models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL,
        null=True, verbose_name=('Country'))
    
    
    department = ChainedForeignKey(
        Department, 
        chained_field="country",
        chained_model_field="country", 
        show_all=False, 
        auto_choose=True,
        default ="",
        blank=True
    )

    city = ChainedForeignKey(
        City, 
        chained_field="department",
        chained_model_field="department", 
        show_all=False, 
        auto_choose=True,
        default ="",
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.name
