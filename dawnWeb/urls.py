"""dawnWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from ecgwebsite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.frontend, name="frontend"),
    path('', include('django.contrib.auth.urls')),
    path('backend/',views.backend, name="backend"),
    path('addpatient',views.addpatient, name="addpatient"),
    path('delete_patient/<str:patient_id>', views.delete_patient, name="delete_patient"),
    path('access_patient/<str:patient_id>', views.access_patient, name="access_patient"),
    path('edit_patient', views.edit_patient, name="edit_patient"),
    path('test', views.test, name="test"),
]
