from django.contrib import admin
from ecgwebsite.models import Patient
# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display =  ['name', 'phone', 'email','age', 'gender', 'create_at']
    search_fields = ['name', 'phone', 'email', 'age']
    list_filter = ['gender']
    list_per_page = 2
admin.site.register(Patient,PatientAdmin)