from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class todo(models.Model):
    status_code=[
        ('C','Completed'),
        ('P','Pending'),
    ]
    priority_code=[
        ('1','1️⃣'),
        ('2','2️⃣'),
        ('3','3️⃣'),
    ]
    title=models.CharField(max_length=50)
    status=models.CharField(max_length=2,choices=status_code)
    date=models.DateTimeField(auto_now_add=TRUE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    priority=models.TextField(choices=priority_code)

