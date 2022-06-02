from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
def upload_to(instance):
    return 'ECGRecord/%s' % (instance.user.user.username)
class ECGRecord(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = "ECGRecoed",null = True)
    title = models.CharField(max_length = 200)
    ecgrecord = models.FileField(upload_to = upload_to)
    detecttime = models.DateTimeField(auto_now = True) 

    def get_user(self):
        return str(self.user.pk)

class Patient(models.Model):
    GENDER = (
        ('F', 'F'),
        ('M', 'M'),
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, null=True, choices=GENDER)
    note = models.TextField(blank=True)
    create_at = models.DateTimeField(default=timezone.now)

def __str__(self):
    return self.name