from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    p=tblpackage.objects.all().order_by("-id")[0:4]
    d={"packages":p}
    if request.method=="POST":
        Name=request.POST.get("name")
        Mobile=request.POST.get("mob")
        Email=request.POST.get("email")
        Message=request.POST.get("msg")

        tblcontact(name=Name,email=Email,mobile=Mobile,message=Message).save()
        return HttpResponse("<script>alert('Data Saved Successfully');location.href='/index/'</script>")
  
    return render(request,"index.html",d)

def about(request):
    return render(request,"about.html")

def team(request):
    data=tblteam.objects.all() 
    d={"team":data}

    return render(request,"team.html",d)

def gallery(request):
      data=tblgallery.objects.all()
      d={"gal":data}
      return render(request,"gallery.html",d)

def category(request):
    x=request.POST.get("search")
    bdata=""
    if x:
        bdata=tblblogs.objects.all().filter(Q(city__icontains=x) | Q(title__icontains=x) | Q(description__icontains=x) | Q(name__icontains=x))
    else:
        bdata=tblblogs.objects.all().order_by("-id")
    data=tblcity.objects.all().order_by("-id")
    
    d={"cities":data,"blogs":bdata,}
    return render(request,"category.html",d)

def services(request):
    return render(request,"services.html")

def login(request):
    
    if request.method=="POST":
        email=request.POST.get("email")#abc@gmail.com
        password=request.POST.get("passwd")#1
        x=tblregister.objects.all().filter(email=email,password=password)
        if x.count()==1:
            request.session["name"]=str(x[0].name)
            request.session["userpic"]=str(x[0].picture)
            request.session["email"]=email
            return HttpResponse("<script>location.href='/blogger/package/'</script>")
        else:
            return HttpResponse("<script>alert('Your Email Id or Password is Incorrect..');location.href='/login/'</script>")
    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        Name=request.POST.get("name")
        Email=request.POST.get("email")
        Mobile=request.POST.get("mob")
        Password=request.POST.get("passwd")
        Address=request.POST.get("address")
        Picture=request.FILES["fu"]
        tblregister(name=Name,email=Email,mobile=Mobile,password=Password,address=Address,picture=Picture,regdate=datetime.now().date()).save()
        return HttpResponse("<script>alert('You are Register Successfully..');location.href='/register/'</script>")

    return render(request,"register.html")

def package(request):
    pdata=tblpackage.objects.all().order_by("-id")
    d={"packages":pdata}
    return render(request,"package.html",d)

def logout(request):
    return render(request,"logout.html")

def contact(request):
    return render(request,"contact.html")

