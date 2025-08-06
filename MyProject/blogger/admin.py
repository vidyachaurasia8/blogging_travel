from django.contrib import admin
from .models import *

# Register your models here.


class tblbookingAdmin(admin.ModelAdmin):
    list_display=("id","username","email","packagename","pprice","totalprice","npeople","no_of_days","booking_date","bookingdatefor","time")
admin.site.register(tblbooking,tblbookingAdmin)    

