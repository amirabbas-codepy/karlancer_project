from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=11, null=True)

class SystemSole(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    descripitions = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    price = models.IntegerField()
    status = models.BooleanField(default=True)
    image = models.FileField(upload_to='./media/movie')
    connection_path = models.CharField(max_length=13, null=True)
    
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    adv = models.ForeignKey(SystemSole, on_delete=models.CASCADE)