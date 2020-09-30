from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
class signup(models.Model):
    first_name=models.CharField(max_length=20)
    middle_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    dob=models.DateTimeField(default=timezone.now,blank=True)
    gender=models.CharField(max_length=2)
    date_created=models.DateTimeField()
    
    def __str__(self):
        return self.first_name