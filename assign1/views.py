from django.shortcuts import render,redirect
from .models import signup
from datetime import datetime
# Create your views here.
def register(request):

     if request.method =='POST':
        first_name =request.POST['firstName']
        last_name=request.POST['lastName']
        email=request.POST['email']
        password=request.POST['pass']
        dob=request.POST['dob']
        gender=request.POST['gender'] 
        middle_name=request.POST['middleName']
        
       

        user =signup(first_name=first_name,middle_name=middle_name,last_name=last_name,email=email,password=password,dob=dob,gender=gender,date_created=datetime.now())
        user.save()
        print("user saved")
        return render(request,'welcome.html',{'name':first_name})
     else :
        return render(request,'signup.html')
