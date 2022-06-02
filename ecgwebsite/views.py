from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

from ecgwebsite.models import Patient
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
# frontend
def frontend(request):
    return render(request, "home.html")
# backend
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def backend(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_patient_list = Patient.objects.filter(
            Q(name=q) | Q(phone=q) | Q(email=q) | Q(age=q) |Q(gender=q) |Q(note=q)
        ).order_by('create_at')
    else:
        all_patient_list = Patient.objects.all().order_by('create_at')
    paginator = Paginator(all_patient_list, 10)
    page = request.GET.get('page')
    all_patient = paginator.get_page(page)
    return render(request, "backend.html", {"patients":all_patient})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def addpatient(request):
    if request.method == "POST":
        
        email = request.POST['email']
        if Patient.objects.filter(email=email).exists():
            messages.error(request, "Email already registered !")
            return render(request, 'add.html')

        elif ( request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('age') and request.POST.get('gender') )or request.POST.get('note'):
            patient = Patient()
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            patient.save()
            messages.success(request, "Patient added successfully!")
            return redirect('/backend')
        else:
            patient = Patient()
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            print(patient.name)
            print(patient.phone)
            print(patient.email)
            print(patient.age)
            print(patient.gender)
            print(patient.note)

            print("values error")
            return redirect('/backend/')
            
    else:
        return render(request, "add.html")

#Fun of delete patients
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def delete_patient(request, patient_id):
    patient = Patient.objects.get(id = patient_id)
    patient.delete()
    messages.success(request, "Patient removed successfully !")
    return redirect('/backend')

#Fun of access patients
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def access_patient(request, patient_id):
    patient = Patient.objects.get(id = patient_id)
    if patient != None:
        return render(request, "edit.html", {'patient':patient})

#Fun of access patients
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def edit_patient(request):
    if request.method == "POST":
        patient = Patient.objects.get(id = request.POST.get('id'))
        if patient != None:
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            patient.save()
            
            messages.success(request, "Patient update successfully !")
            return HttpResponseRedirect('/backend')

def test(request):
        return render(request, "test.html")