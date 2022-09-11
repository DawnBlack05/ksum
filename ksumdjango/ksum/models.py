from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class User(models.Model):
    Student_number = models.IntegerField()
    Student_password = models.CharField(max_length=20) # 패스워드는 20자 이하

    def __str__(self):
        return str(self.Student_number)

class borrow(models.Model):
    umbrella_number = models.IntegerField(default=0)
    borrowed = models.BooleanField(default=False)
    borrowed_by = models.IntegerField(default=0)
    return_date = models.DateField(default = timezone.now)
    

    def __str__(self):
        return '{}번 우산'.format(self.umbrella_number)
