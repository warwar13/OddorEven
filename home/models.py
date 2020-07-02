from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.TextField(max_length=200,blank=True)
    birthday = models.DateField(null=True, blank=True)
    balance = models.IntegerField(default=100)

    def __str__(self):
        return  self.user.username

