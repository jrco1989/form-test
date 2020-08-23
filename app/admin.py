from django.contrib import admin
from .models import Registry, Country, City, Department
# Register your models here.
admin.site.register(Registry)
admin.site.register(Country)
admin.site.register(Department)
admin.site.register(City)
