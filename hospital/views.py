from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,User


def aboutus(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def index(request):
    doctor=Doctor.objects.all()
    patient=Patient.objects.all()
    appointment=Appointment.objects.all()
    d=0
    p=0
    a=0
    for i in doctor:
        d+=1
    for i in patient:
        p+=1
    for i in appointment:
        a+=1

    d1={'d':d,'p':p,'a':a}
    return render(request,'index.html',d1)

def login_view(request):
    error=""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        c12=User.objects.filter(username=p)
        category1=Register.objects.filter(username=c12,is_doctor='Patient')
        try:
            if user.is_staff:
                login(request,user)
                error="no"
                
            elif Register.objects.filter(username=c12,is_doctor='Patient') is not None:  
                login(request,user)
                error="no1"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}
    return render(request,'login.html',d)

def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('hospital:login')
    logout(request)
    return redirect('hospital:login')

def view_doctor(request):
    if not request.user.is_staff:
        return redirect('hospital:login')
    doc = Doctor.objects.all()
    d={'doc':doc}
    return render(request,'view_doctor.html',d)

def add_doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('hospital:login')
    if request.method == 'POST':
        u = request.POST['uname']
        e = request.POST['email']
        s = request.POST['special']
        sa = request.POST['salary']
        try:
            Doctor.objects.create(name=u,email=e,special=s,salary=sa)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'add_doctor.html',d)

def delete_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('hospital:login')
    doctor=Doctor.objects.get(id=pid)
    doctor.delete()
    return render(request,'view_doctor.html')

def view_patient(request):
    if not request.user.is_staff:
        return redirect('hospital:login')
    doc = Patient.objects.all()
    d={'doc':doc}
    return render(request,'view_patient.html',d)

def add_patient(request):
    error=""
    """
    if not request.user.is_staff:
        return redirect('hospital:login')
    """
    if request.method == 'POST':
        u = request.POST['uname']
        m = request.POST['mobile']
        a= request.POST['address']
        s = request.POST['symptoms']
        b = request.POST['age']
        f=request.POST['fees']
        try:
            Patient.objects.create(name=u,mobile=m,address=a,symptoms=s,age=b,fees=f)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'add_patient.html',d)

def delete_patient(request,pid):
    if not request.user.is_staff:
        return redirect('hospital:login')
    patient=Patient.objects.get(id=pid)
    patient.delete()
    return render(request,'view_patient.html')

def view_appointment(request):
    if not request.user.is_staff:
        return redirect('hospital:login')
    appoint = Appointment.objects.all()
    d={'appoint':appoint}
    return render(request,'view_appointment.html',d)

def add_appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('hospital:login')
    doctor1=Doctor.objects.all()
    patient1=Patient.objects.all()
    if request.method == 'POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t = request.POST['time']
        
        doctor12=Doctor.objects.filter(name=d).first()
        patient12=Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor12,patient=patient12,date1=d1,time1=t)
            error="no"
        except:
            error="yes"
    d={'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'add_appointment.html',d)
    from django.contrib import messages
def delete_appointment(request,pid):
    if not request.user.is_staff:
        return redirect('hospital:login')
    appointment=Appointment.objects.get(id=pid)
    appointment.delete()
    return render(request,'view_appointment.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        c=request.POST['category']
        p=request.POST['username']
        
        if form.is_valid():
            user = form.save()
            c12=User.objects.filter(username=p).first()
            Register.objects.create(username=c12,is_doctor=c)
            return redirect('hospital:login')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})
"""
   error=""
    if request.method == 'POST':
        username=request.POST['username']
        pass1=request.POST['password1']
        pass2=request.POST['password2']

        if pass1 == pass2:
            Register_Patient.objects.create(username=username,password1=pass1,password2=pass2)
            error="no"
        else:
            error="yes"
    d={'error':error}
    return render(request,'register_patient.html',d)

"""