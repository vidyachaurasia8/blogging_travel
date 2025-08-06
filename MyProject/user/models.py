from django.db import models

# Create your models here.
class tblcontact(models.Model):
    name=models.CharField(max_length=70,null=True)
    email=models.EmailField(max_length=100,null=True)
    mobile=models.CharField(max_length=20,null=True)
    message=models.TextField(null=True)

class tblgallery(models.Model):
        title=models.CharField(max_length=50)
        picture=models.ImageField(upload_to="static/gallery/",null=True)

class tblteam(models.Model):
        name=models.CharField(max_length=100,null=True)
        picture=models.ImageField(upload_to="static/images/",null=True)
        post=models.CharField(max_length=100,null=True)
        experiences=models.TextField(null=True)
################################# 

class tblcity(models.Model):
        cityname=models.CharField(max_length=60,null=True)
        picture=models.ImageField(upload_to="static/city/",null=True,blank=True)
        def __str__(self):
            return self.cityname

class tblblogs(models.Model):
        name=models.CharField(max_length=50,null=True)
        email=models.CharField(max_length=50,null=True)
        user_pic=models.CharField(max_length=200,null=True)
        title=models.TextField(null=True) 
        description=models.TextField(null=True)
        picture=models.ImageField(upload_to="static/blogs/",null=True,blank=True)
        city=models.CharField(max_length=50,null=True)
        posteddate=models.CharField(max_length=100,null=True) 

class tblregister(models.Model):
        name=models.CharField(max_length=50,null=True)
        email=models.EmailField(primary_key=True,max_length=100,default="")
        mobile=models.CharField(max_length=20,null=True)
        picture=models.ImageField(upload_to="static/userpic",null=True,blank=True)
        password=models.CharField(max_length=50,null=True)
        address=models.TextField(null=True)
        regdate=models.DateField(null=True) 

class tblpackage(models.Model):
        package_name=models.CharField(max_length=50,null=True)
        title=models.TextField(null=True)
        package_info=models.TextField(null=True)
        picture=models.ImageField(upload_to="static/package/",null=True,blank=True)
        price=models.FloatField(null=True)
        discounted_price=models.FloatField(null=True)
        posted_date=models.DateField(null=True)
        city=models.ForeignKey(tblcity,on_delete=models.CASCADE)


                                           



   


