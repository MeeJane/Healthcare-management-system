"""
URL configuration for project_healthcare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from django.conf.urls import url
from . import views
urlpatterns = [
    
    path('about',views.about),
    path('contact',views.contact),
    path('',views.home,name='home'),
    path('pat_log_met',views.pat_log_met,name='pat_log_met'),
    path('pat_register',views.pat_register,name='pat_register'),
    path('doc_log_met',views.doc_log_met,name='doc_log_met'),
    path('doc_register',views.doc_register,name='doc_register'),
    # path('index', views.index,name='index'),
    # path('home', views.home,name='home'),
    path('predoctor', views.predoctor, name='predoctor'),
    path('prepatient', views.prepatient, name='prepatient'),
    path('doctors_list', views.doctors_list, name='doctors_list'),
    path('doctor_desk', views.doctor_desk, name='doctor_desk'),
    # path('doc_id', views.doc_id, name='doc_id'),
    path('doc_profile', views.doc_profile, name='doc_profile'),
    path('docid_view', views.docid_view, name='docid_view'),
    path('patient_desk', views.patient_desk, name='patient_desk'),
    path('patients_list', views.patients_list, name='patients_list'),
    path('doctor_signup', views.doctor_signup, name='doctor_signup'),
    path('doctor_view', views.doctor_view, name='doctor_view'),
    path('doctor_edit/<int:DID>',views.doctor_edit,name='doctor_edit'),
    path('doctor_update/<int:DID>',views.doctor_update,name='doctor_update'),
    path('adm_log_met',views.adm_log_met,name='adm_log_met'),
    path('adm_register',views.adm_register,name='adm_register'),
    path('admin_page', views.admin_page, name='admin_page'),
    path('patient_signup', views.patient_signup, name='patient_signup'),
    path('patient_view', views.patient_view, name='patient_view'),
    path('patient_edit/<int:PID>',views.patient_edit,name='patient_edit'),
    path('patient_update/<int:PID>',views.patient_update,name='patient_update'),
    path('doc_delete/<int:DID>',views.doc_delete,name='doc_delete'),
    path('pat_delete/<int:PID>',views.pat_delete,name='pat_delete'),
    # path('doc_prof_edit', views.doc_prof_edit, name='doc_prof_edit'),
    path('doc_prof_update', views.doc_prof_update, name='doc_prof_update'),
    path('doctor_adm_update/<int:DID>', views.doctor_adm_update, name='doctor_adm_update'),
    path('doctor_adm_edit/<int:DID>', views.doctor_adm_edit, name='doctor_adm_edit'),    
    path('patient_adm_update/<int:PID>', views.patient_adm_update, name='patient_adm_update'),
    path('patient_adm_edit/<int:PID>', views.patient_adm_edit, name='patient_adm_edit'),
    path('doc_id', views.doc_id, name='doc_id'),
    path('pat_prof_update', views.pat_prof_update, name='pat_prof_update'),
    path('pat_id', views.pat_id, name='pat_id'),
    path('spec_search', views.spec_search, name='spec_search'),
]

