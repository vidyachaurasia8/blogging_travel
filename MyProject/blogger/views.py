from django.shortcuts import render,redirect
from user.models import *
from .models import *
from datetime import datetime
from django.http import HttpResponse


# Create your views here.

def index(request):
    username=request.session.get("name")
    email=request.session.get("email")
    price=request.GET.get("dprice")
    package=request.GET.get("pkg")
    p=tblpackage.objects.all()
    if request.method=="POST":
        ndays=request.POST.get("ndays")
        npeople=request.POST.get("npeople")
        ndate=request.POST.get("ndate")
        ntime=request.POST.get("ntime")
        totalprice=float(price)*float(npeople)
        tblbooking(username=username,email=email,packagename=package,pprice=price,totalprice=totalprice,npeople=npeople,no_of_days=ndays,bookingdatefor=ndate,time=ntime,booking_date=datetime.now().date()).save()
        return HttpResponse("<script>alert('your package has booked successfully..');location.href='/blogger/package/';</script>")
        
    d={"packages":p,"dprice":price,"package":package}
    return render(request,"blogger/index.html",d)

def dashboard(request):
    return render(request,"blogger/dashboard.html")

def myblogs(request):
    email=request.session.get("email")
    username=request.session.get("name")
    userpic=request.session.get("userpic")
    bdata=tblblogs.objects.all().filter(email=email).order_by("-id")
    d={}
    if request.method=="POST":
        title=request.POST.get("title")
        info=request.POST.get("info")
        city=request.POST.get("city")
        picture=request.FILES["fu"]
        tblblogs(name=username,email=email,user_pic=userpic,title=title,description=info,city=city,picture=picture,posteddate=datetime.now().date()).save()
        d={"success":True,}
    d["blogs"]=bdata    


    return render(request,"blogger/myblogs.html",d)

def history(request):
    email=request.session.get("email")
    data=tblbooking.objects.all().filter(email=email)
    d={"bdata":data}
    return render(request,"blogger/history.html",d)

def profile(request):
    email=request.session.get("email")
    data=tblregister.objects.all().filter(email=email)
    if request.method=="POST":
        Name=request.POST.get("name")
        Mobile=request.POST.get("mob")
        Password=request.POST.get("password")
        Address=request.POST.get("address")
        Picture=request.FILES["fu"]
        tblregister.objects.filter(email=email).update(name=Name,mobile=Mobile,password=Password,address=Address,picture=Picture,regdate=datetime.now().date())
        return HttpResponse("<script>alert('Your Profile has updated Successfully');localion.href='/blogger/profile/'</script>")
    d={"pdata":data}
    return render(request,"blogger/profile.html",d)

def signout(request):
     user=request.session.get("email")
     if user:
        del request.session["email"]
        return redirect("/login/")
     return render(request,"blogger/signout.html")


