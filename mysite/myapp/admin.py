from django.contrib import admin

# Register your models here.

from .models import Person
admin.site.register(Person)

from .models import Hire
admin.site.register(Hire)