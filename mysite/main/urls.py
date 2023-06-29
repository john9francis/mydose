from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/patient", views.patient_login, name="patient_login"),
    path("login/patient/patient_portal_redirect", views.patient_portal, name="patient_portal"),
    path("login/doctor", views.doctor_login, name="doctor_login"),
    path("login/doctor/doctor_portal_redirect", views.doctor_portal, name="doctor_portal")
]