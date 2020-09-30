from django.shortcuts import render
from .models import contact_us
# Create your views here.

def messages(request):

    if request.method =='POST':
        name =request.POST['name']
        subject=request.POST['subject']
        email=request.POST['email']
        message=request.POST['message']
        query=request.POST['query']
        
        user =contact_us(name=name,subject=subject,message=message,email=email,query=query)
        user.save()
        print("query saved")
        return render(request,'contact.html')
    else:
        return render(request,'contact.html')

def show(request):
    all_messsages=contact_us.objects.all()
    return render(request,'messages.html',{'messages':all_messsages})