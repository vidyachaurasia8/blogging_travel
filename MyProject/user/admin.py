from django.contrib import admin
from .models import *

# Register your models here.
class tblcontactAdmin(admin.ModelAdmin):
    list_display=("name","email","mobile","message")
admin.site.register(tblcontact,tblcontactAdmin)

class tblgalleryAdmin(admin.ModelAdmin):
    list_display=("title","picture")
admin.site.register(tblgallery,tblgalleryAdmin)    

class tblteamAdmin(admin.ModelAdmin):
    list_display=("name","picture","post","experiences")
admin.site.register(tblteam,tblteamAdmin)

class tblcityAdmin(admin.ModelAdmin):
    list_display=("id","cityname","picture") 
admin.site.register(tblcity,tblcityAdmin) 

class tblblogsAdmin(admin.ModelAdmin):
    list_display=("id","name","email","user_pic","title","description","picture","city","posteddate")
admin.site.register(tblblogs,tblblogsAdmin) 

class tblregisterAdmin(admin.ModelAdmin):
    list_display=("name","email","mobile","password","picture","address","regdate")
admin.site.register(tblregister,tblregisterAdmin)

class tblpackageAdmin(admin.ModelAdmin):
    list_display=("id","package_name","title","package_info","price","discounted_price","picture","posted_date","city")
admin.site.register(tblpackage,tblpackageAdmin)


