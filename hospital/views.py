from django.shortcuts import render,redirect
from .models import Patients
from .models import Doctors
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# # from .models import ViewDoctors
# from .forms import DoctorForm
from .forms import DoctorForm
from .forms import PatientForm
from .forms import DocId_Form,Doc_IdForm,PatId_Form,Pat_IdForm,Dep_Form
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Doc_Register,Adm_Register
from .models import Pat_Register

from .forms import Doc_Reg_Form, Doc_LoginForm,Adm_Reg_Form,Adm_LoginForm
from .forms import Pat_Reg_Form, Pat_LoginForm

appname='hospital'


# Create your views here.
def home(request):
    # return HttpResponse('Homepage')
     return render(request, 'hospital/home.html')

def about(request):
    # return HttpResponse('About')
    return render(request, 'hospital/about.html')
def contact(request):
    # return HttpResponse('Contact')
    return render(request, 'hospital/contact.html')

 


# def index(request):
#     return render(request, 'hospital/index.html')


# def home(request):
#     return render(request, 'hospital/home.html')


# @login_required(login_url="/accounts/login/")
def doctor_signup(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/hospital/doc_register')
            except:
                pass
    else:
        form = DoctorForm()
    return render(request, 'hospital/docform.html',{'form': form})


# def doc_id(request):
#     if request.method=='POST':
#         form=DocId_Form(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('hospital/index')
#             except:
#                 pass
#     else:
#         form=DocId_Form()
#     return render(request,'hospital/docidform.html',{'form':form})


def docid_view(request):

    return render(request,'hospital/docidform.html')


def doctor_view(request):
    docs=Doctors.objects.all()
    return render(request,'hospital/docview.html',{'docs':docs})

def doctor_adm_edit(request,DID):
    docs=Doctors.objects.get(DID=DID)
    return render(request,'hospital/docupdate.html',{'docs':docs})

def patient_adm_edit(request,PID):
    pats=Patients.objects.get(PID=PID)
    return render(request,'hospital/patupdate.html',{'pats':pats})


def doctor_edit(request,DID):
    docs=Doctors.objects.get(DID=DID)
    return render(request,'hospital/docupdate.html',{'docs':docs})


def doctor_update(request,DID):
    docs=Doctors.objects.get(DID=DID)
    if request.method=="POST":
        form=DoctorForm(request.POST,instance=docs)
        if form.is_valid():
            try:
                form.save()
                return redirect('/hospital/doctor_desk')
            except Exception:
                print('Failure')
    return render(request,'hospital/docupdate.html',{'docs':docs})

def doctor_adm_update(request,DID):
    docs=Doctors.objects.get(DID=DID)
    if request.method=="POST":
        form=DoctorForm(request.POST,instance=docs)
        if form.is_valid():
            try:
                form.save()
                return redirect('/hospital/doctor_view')
            except Exception:
                print('Failure')
    return render(request,'hospital/doc_admupdate.html',{'docs':docs})

def patient_adm_update(request,PID):
    pats=Patients.objects.get(PID=PID)
    if request.method=="POST":
        form=PatientForm(request.POST,instance=pats)
        if form.is_valid():
            try:
                form.save()
                return redirect('/hospital/patient_view')
            except Exception:
                print('Failure')
    return render(request,'hospital/pat_admupdate.html',{'pats':pats})




def doc_delete(request,DID):
    doc=Doctors.objects.get(DID=DID)
    doc.delete()
    return redirect('/hospital/doctor_view')


def doc_profile(request):
   id=int(request.POST["did"])
   docs = Doctors.objects.all()
   return render(request,'hospital/docprofile.html',{'id':id,'docs':docs})


# @login_required(login_url="/accounts/doc_login")
def admin_page(request):
    return render(request, 'hospital/admin.html')


def patient_signup(request):
    if request.method=='POST':
        form=PatientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/hospital/pat_register')
            except:
                pass
    else:
        form=PatientForm()
    return render(request, 'hospital/patform.html',{'form': form})


def patient_view(request):
    pats=Patients.objects.all()
    return render(request, 'hospital/patview.html',{'pats': pats})


def patient_edit(request,PID):
    pats=Patients.objects.get(PID=PID)
    return render(request,'hospital/patupdate.html',{'pats':pats})
# def doctor_edit(request,DID):
#     docs=Doctor_Signup.objects.get(DID=DID)
#     return render(request,'hospital/docupdate.html',{'docs':docs})


def patient_update(request,PID):
    pats=Patients.objects.get(PID=PID)
    if request.method == "POST":
        form = PatientForm(request.POST,instance=pats)
        if form.is_valid():
            try:
                form.save()
                return redirect('/hospital/patient_desk')
            except Exception:
                print("Failure")
    return render(request,'hospital/patupdate.html',{'pats':pats})

def doctor_update(request,DID):
    docs=Doctors.objects.get(DID=DID)
    if request.method=="POST":
        form=DoctorForm(request.POST,instance=docs)
        if form.is_valid():
            try:
                form.save()
                return redirect('/hospital/doctor_desk')
            except Exception:
                print('Failure')
    return render(request,'hospital/docupdate.html',{'docs':docs})


def pat_delete(request,PID):
    pat=Patients.objects.get(PID=PID)
    pat.delete()
    return redirect('/hospital/patient_view')

# @login_required(login_url="/accounts/doc_login")
def predoctor(request):
    return render(request,'hospital/predoctor.html')

def doctors_list(request):
    docs = Doctors.objects.all()
    return render(request,'hospital/doctorslist.html',{'docs': docs})

def patients_list(request):
    pats = Patients.objects.all()
    return render(request, 'hospital/patientslist.html', {'pats': pats})

def doctor_desk(request):
    return render(request,'hospital/doctorsdesk.html')

def patient_desk(request):
    return render(request,'hospital/patientsdesk.html')


# @login_required(login_url="/accounts/doc_login")
def prepatient(request):
    return render(request,'hospital/prepatient.html')

# Create your views here.


# Create your views here.
Pat_Reg_Form


# Create your views here.
def doc_register(request):
    
    if request.method=="POST":
        reg=Doc_Reg_Form(request.POST)
        if reg.is_valid():
            reg.save()
            return redirect('/hospital/doctor_desk')
        else:
            pass
    else:
        reg=Doc_Reg_Form()
    return render(request,'hospital/doc_register.html', {'form':reg}) 

def doc_login(request):
    return render(request,'hospital/doc_login.html')

# def home(request):
#     reg=RegisterForm()
#     trans=TransForm()
#     return render(request, 'home.html', {'trans':trans, 'reg':reg})     

def doc_log_met(request):
    if request.method=="POST":
        if Doc_Register.objects.filter(Username=request.POST.get('Username'),Password=request.POST.get('Password')).exists():
            reg=Doc_Register.objects.get(Username=request.POST.get('Username'),Password=request.POST.get('Password'))
            
            #trans=Transcation.objects.filter()
            # return render(request, 'home.html', {'trans':trans,'reg':reg})
            return redirect('/hospital/doctor_desk')
        else:
            context={'msg':'Invalid username and password'}
            return render(request,'hospital/doc_login.html',context) 
    else:
        reg= Doc_LoginForm()
    return render(request,'hospital/doc_login.html', {'reg':reg})



def pat_register(request):
    
    if request.method=="POST":
        reg=Pat_Reg_Form(request.POST)
        if reg.is_valid():
            reg.save()
            return redirect('/hospital/spec_search')
        else:
            pass
    else:
        reg=Pat_Reg_Form()
    return render(request,'hospital/pat_register.html', {'form':reg}) 

def adm_register(request):
    
    if request.method=="POST":
        reg=Adm_Reg_Form(request.POST)
        if reg.is_valid():
            reg.save()
            return redirect('/hospital/admin_page')
        else:
            pass
    else:
        reg=Pat_Reg_Form()
    return render(request,'hospital/adm_register.html', {'form':reg})

def pat_login(request):
    return render(request,'hospital/pat_login.html')
def adm_login(request):
    return render(request,'hospital/adm_login.html')

# def home(request):
#     reg=RegisterForm()
#     trans=TransForm()
#     return render(request, 'home.html', {'trans':trans, 'reg':reg})     

def pat_log_met(request):
    if request.method=="POST":
        if Pat_Register.objects.filter(Username=request.POST.get('Username'),Password=request.POST.get('Password')).exists():
            reg= Pat_Register.objects.get(Username=request.POST.get('Username'),Password=request.POST.get('Password'))
            #trans=Transcation.objects.filter()
            # return render(request, 'home.html', {'trans':trans,'reg':reg})
            return redirect('/hospital/patient_desk')
        else:
            context={'msg':'Invalid username and password'}
            return render(request,'hospital/pat_login.html',context) 
    else:
        reg= Pat_LoginForm()
    return render(request,'hospital/pat_login.html', {'reg':reg})

def adm_log_met(request):
    if request.method=="POST":
        if Adm_Register.objects.filter(Username=request.POST.get('Username'),Password=request.POST.get('Password')).exists():
            reg= Adm_Register.objects.get(Username=request.POST.get('Username'),Password=request.POST.get('Password'))
            #trans=Transcation.objects.filter()
            # return render(request, 'home.html', {'trans':trans,'reg':reg})
            return redirect('/hospital/admin_page')
        else:
            context={'msg':'Invalid username and password'}
            return render(request,'hospital/adm_login.html',context) 
    else:
        reg= Adm_LoginForm()
    return render(request,'hospital/adm_login.html', {'reg':reg})


# def doc_prof_edit(request):
#     D_d =int(request.POST["doc_id"])
#     docs=Doctors.objects.get(DID=D_d)
#     return render(request,'hospital/docprof.html',{'docs':docs})


def doc_prof_update(request):
    
    if request.method=="POST":
        if Doctors.objects.filter(DID=request.POST.get('DID')).exists():
            docs=Doctors.objects.get(DID=request.POST.get('DID'))
            # docs=Doctors.objects.get(Name=request.POST.get('Name'),DID=request.POST.get('DID'),speciality=request.POST.get('speciality'),mobile_no=request.POST.get('mobile_no'),address=request.POST.get('address'))
            # return redirect('/hospital/patient_desk')
            # docs=Doctors.objects.all()
            # docs=Doctors.objects.filter()
            # return render(request,'hospital/docprof.html',{'docs':docs})
            print(docs)
            return render(request,'hospital/docprof.html',{'docs':docs})
        else:
            context={'msg':'ID doesnot Exists'}
            return render(request,'hospital/doc_id.html',context) 
    else:
        docs= Doc_IdForm()
    return render(request,'hospital/doc_id.html', {'docs':docs})



def pat_prof_update(request):
    
    if request.method=="POST":
        if Patients.objects.filter(PID=request.POST.get('PID')).exists():
            pats=Patients.objects.get(PID=request.POST.get('PID'))
            # docs=Doctors.objects.get(Name=request.POST.get('Name'),DID=request.POST.get('DID'),speciality=request.POST.get('speciality'),mobile_no=request.POST.get('mobile_no'),address=request.POST.get('address'))
            # return redirect('/hospital/patient_desk')
            # docs=Doctors.objects.all()
            # docs=Doctors.objects.filter()
            # return render(request,'hospital/docprof.html',{'docs':docs})
            
            return render(request,'hospital/patprof.html',{'pats':pats})
        else:
            context={'msg':'ID doesnot Exists'}
            return render(request,'hospital/pat_id.html',context) 
    else:
        pats= Pat_IdForm()
    return render(request,'hospital/pat_id.html', {'pats':pats})
           
            
            
    
    # D_d =request.POST['doc_id']

    
    # if request.method=="POST":
    #     # trans=Doc_LoginForm(request.POST)
    #     form=DoctorForm(request.POST,instance=D_d)
    #     if form.is_valid():
    #         try:
    #             form.save()
    #             return redirect('/hospital/predoctor')
    #         except Exception:
    #             print('Failure')
   

def doc_id(request):
      return render(request, 'hospital/doc_id.html')        
def pat_id(request):
      return render(request, 'hospital/pat_id.html')


def spec_search(request):
    
    if request.method=="POST":
        if Doctors.objects.filter(Department=request.POST.get('Department')).exists():
            # docs=Doctors.objects.get(Department=request.POST.get('Department'))
            # docs=Doctors.objects.get(Name=request.POST.get('Name'),DID=request.POST.get('DID'),speciality=request.POST.get('speciality'),mobile_no=request.POST.get('mobile_no'),address=request.POST.get('address'))
            # return redirect('/hospital/patient_desk')
            # docs=Doctors.objects.all()
            docs=Doctors.objects.filter(Department=request.POST.get('Department'))
            # return render(request,'hospital/docprof.html',{'docs':docs})
            # print(docs)
            return render(request,'hospital/availdocs.html',{'docs':docs})
        else:
            context={'msg':'Doctor not available'}
            return render(request,'hospital/pat_dep.html',context) 
    else:
        docs= Dep_Form()
    return render(request,'hospital/pat_dep.html', {'docs':docs})     