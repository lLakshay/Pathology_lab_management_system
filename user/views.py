from email import message
from multiprocessing import context
import re
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import Book, Patients
from .models import LabTest
from .models import BookedTest
from .models import Book
from datetime import datetime
from django.db.models import DateTimeField
from django.db.models.functions import Trunc
import time
input_datetime_format = "%Y-%m-%d %I:%M %p"

# from PLMS.models import Patients 
# Create your views here. render(request,'user/login_register.html',context)


# def loginPage(request):
#   if request.user.is_authenticated:
#     return redirect('home')
#   if request.method=='POST':
#     username=request.POST.get('email')
#     password=request.POST.get('password')

#     try:
#       user=User.objects.get(username=username)
#     except:
#       messages.error(request,'User does not exits ')
#     user = authenticate(request,username=username,password=password)

#     if user is not None:
#       login(request,user)
#       return redirect('home')
#     else:
#       messages.error(request,'Email or password does not exists ')
#   context={}
#   return render(request,'user/login_register.html')

def loginPage(request):
  if request.session.get('user_id'):
    return redirect('home')
  if request.method=='POST':
    try:
      userdetails=Patients.objects.get(patient_email=request.POST.get('email'),patient_password=request.POST.get('password'))
      print(userdetails)
      request.session['email']=userdetails.patient_email
      request.session['user_id']=userdetails.patient_id
      return redirect('home')
    except Patients.DoesNotExist as e:
      messages.success(request,'Password invalid')
    
  return render(request,'user/login_register.html')
# @login_required(login_url='login')

def home(request):
  if request.session.get('user_id'):
    test=LabTest.objects.all()
    context={'test':test}
    return render(request,'user/home.html',context)
  else:
    return redirect('login')
  

def logoutUser(request):
  # logout(request)
  try:
    del request.session['email']
    del request.session['user_id']
  except:
    return redirect('login')
  return redirect('login')

def register(request):
  if request.method=='POST':
    print(request.POST)
    Username=request.POST.get('name')
    Email=request.POST.get('email')
    Password=request.POST.get('password')
    dob=request.POST.get('dob')
    phone=request.POST.get('phone')
    gender=request.POST.get('gender')
    Patients(patient_name=Username,patient_email=Email,patient_password=Password,patient_dob=dob,patient_gender=gender,patient_phone_number=phone,patient_status=1).save()
    messages.success(request,'The User '+request.POST.get('name')+'Is saved sucessfullt')
    return render(request,'user/register.html')
  else:
    return render(request,'user/register.html')

def book(request,test_name):
  if request.session.get('user_id'):
    if request.method=='POST':
      
      datetime_str=f"{request.POST.get('date')} {request.POST.get('time')}"
      date = datetime.strptime(datetime_str, input_datetime_format)
      p_id=request.session.get('user_id')
      patients=Patients.objects.get(patient_id=p_id)
      bt=BookedTest(p_id=patients,b_date=date,tests=test_name,booking_status='Requested')
      bt.save()
      messages.success(request,'Booked Suceesfully')
      return redirect('home')
    # test_name=request.POST.get('email')
    print(test_name)
    context={'test_name': test_name}
    return render(request,'user/booking.html',context)
  else:
    return redirect('login')

def history(request):
   if request.session.get('user_id'):
    p_id=request.session.get('user_id')
    bookingdata=BookedTest.objects.filter(p_id=p_id).order_by(
    Trunc('b_date', 'date', output_field=DateTimeField()).desc(),
    '-p_id')
    status={'Requested':0,'Booked':26,'Testing':50,'Completed':100}
    context={'booking': bookingdata,'status':status}
    return render(request,'user/booking-history.html',context)
   else:
     return redirect('login')
def profile(request):
  if request.session.get('user_id'):
    p_id=request.session.get('user_id')
    profile=Patients.objects.get(patient_id=p_id)
    context={'profile': profile}

    if request.method=="POST":
      Username=request.POST.get('name')
      if request.POST.get('pass1') != request.POST.get('pass2'):
        messages.error(request,'The Password does not match')
        return render(request,'user/profile.html')

      Password=request.POST.get('pass2')
   
      phone=request.POST.get('phone')
      gender=request.POST.get('gender')
      up_pat=Patients.objects.get(patient_id=p_id)
      up_pat.patient_name=Username
      if request.POST.get('pass2')!="":
         up_pat.patient_password=Password
      if request.POST.get('date')!="":
        up_pat.patient_dob=dob=request.POST.get('date')
      up_pat.patient_gender=gender
      up_pat.patient_phone_number=phone
      up_pat.save()
      messages.success(request,'The User '+request.POST.get('name')+'Is saved sucessfullt')


    return render(request,'user/profile.html',context)
  else:
    return redirect('login')

def cancel(request,b_id):
  if request.session.get('user_id'):
      p_id=request.session.get('user_id')
      BookedTest.objects.get(book_id=b_id).delete()
      messages.success(request,'The booking is cancelled sucessfullt')
      return redirect('history')

def haematology(request):
  if request.session.get('user_id'):
    p_id=request.session.get('user_id')
    haemoglobin=request.POST.get('haemoglobin')
    wbc=request.POST.get('wbc')
    haematocrit=request.POST.get('haematocrit')
    rbc=request.POST.get('rbc')
    neutrophilis=request.POST.get('neutrophilis')
    eosinophils=request.POST.get('eosinophils')
    basophils=request.POST.get('basophils')
    lymphocytes=request.POST.get('lymphocytes')
    monocytes=request.POST.get('monocytes')
    esr=request.POST.get('esr')
    bleedingtime=request.POST.get('bleedingtime')
    blesec=request.POST.get('blesec')
    clottingtime=request.POST.get('clottingtime')
    closec=request.POST.get('closec')
    totalplatelet=request.POST.get('totalplatelet')
    
  return render(request,'user/haematology.html')


    
  
  
