from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

appname='accounts'

# Create your views here.
def doc_sign(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/hospital/doctor_desk')
    else:
        form=UserCreationForm()
    return render(request,'accounts/doc_sign.html',{'form':form})

def pat_sign(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/hospital/patient_desk')
    else:
        form=UserCreationForm()
    return render(request,'accounts/pat_sign.html',{'form':form})

def doc_login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid:
            user=form.get_user()
            login(request,user)
            return redirect('/hospital/doctor_desk')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/doc_login.html',{'form':form})

def pat_login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid:
            user=form.get_user()
            login(request,user)
            return redirect('/hospital/patient_desk')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/pat_login.html',{'form':form})


def logoff(request):
    if request.method=='POST':
        logout(request)
        return redirect('/hospital/')
    

