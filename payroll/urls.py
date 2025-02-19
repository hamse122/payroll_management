# payroll/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_payroll, name='payroll_register'),
    path('register/list/', views.payroll_list, name='payroll_list'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('delete/<int:payroll_id>/', views.delete_payroll, name='delete_payroll'),
    path('update/<int:payroll_id>/', views.update_payroll, name='update_payroll'),
]
