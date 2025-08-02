from django import forms
from .models import Doctors,Patients
from .models import Doc_Register,Pat_Register,Adm_Register


class Doc_Reg_Form(forms.ModelForm):
    class Meta:
        model=Doc_Register
        fields="__all__"

class Adm_Reg_Form(forms.ModelForm):
    class Meta:
        model=Adm_Register
        fields="__all__"

class Pat_Reg_Form(forms.ModelForm):
    class Meta:
        model=Pat_Register
        fields="__all__"
        

class Doc_LoginForm(forms.Form):
    
    Username=forms.CharField(max_length=20)
    Password=forms.CharField(max_length=20) 

class Adm_LoginForm(forms.Form):
    
    Username=forms.CharField(max_length=20)
    Password=forms.CharField(max_length=20) 

class Doc_IdForm(forms.Form):
    DID=forms.IntegerField()

class Dep_Form(forms.Form):
    Department=forms.CharField(max_length=100)

class Pat_IdForm(forms.Form):
    PID=forms.IntegerField()

class Pat_LoginForm(forms.Form):
    
    Username=forms.CharField(max_length=20)
    Password=forms.CharField(max_length=20) 


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = '__all__'
        # fields = ['First_name','Last_name','speciality','mobile_no','address']
        # exclude=['Username','Password']


class PatientForm(forms.ModelForm):
    class Meta:
        model=Patients
        fields='__all__'
        # fields = ['First_name','Last_name','speciality','mobile_no','address']
        # exclude=['Username','Password']


class DocId_Form(forms.ModelForm):
    class Meta:
        model:Doctors
        fields=['DID']

class PatId_Form(forms.ModelForm):
    class Meta:
        model:Patients
        fields=['PID']
