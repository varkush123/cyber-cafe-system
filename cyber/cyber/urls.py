"""
URL configuration for cyber project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from home.views import homition
from about.views import aboution
from contact.views import show_message
#from login.views import logination
from login import views 
from dashboard.views import dashnation
from addcus.views import addcunation
from cusdet.views import customer_details
from update.views import update_customer_by_id
from billing.views import calculate_billing
from addcom.views import addcomation
from addcom_details.views import computer_details
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homition,name='home'),
    path('home.html',homition,name='home_html'),
    path('about.html',aboution, name='about_html'),
    path('contact.html',show_message, name='contact_html'),
    path('login.html', views.logination, name='logination'),

    #path('login.html',logination, name='login_html'),
    path('dashboard.html',dashnation, name='dashboard_html'),
    path('addcus.html',addcunation, name='addcus_html'),
    path('cus_det.html',customer_details, name='cus_det_html'),
    path('update.html', update_customer_by_id, name='update_customer_by_id'),
    #path('perform_billing/', views.perform_billing, name='perform_billing'), 
    path('billing.html', calculate_billing, name='calculate_billing'),
    path('addcom.html',addcomation,name='addcom_html'),
     path('com_det.html',computer_details, name='com_det_html'),
]

