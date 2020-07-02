from django.db import models
from home.models import *
from .views import *
from home.views import *

# Create your models here.
class Result(models.Model):
    BET_CHOICES = (
        ('ODD', 'ODD'),
        ('EVEN', 'EVEN'),
    )

    time = models.DateTimeField()
    result = models.CharField(choices=BET_CHOICES,max_length=50, null=True,blank=True)


    def __str__(self):
        return self.result

class Bet(models.Model):
    BET_CHOICES = (
        ('ODD', 'ODD'),
        ('EVEN', 'EVEN'),
    )
    WIN_OR_LOSE = (
        ('WIN', 'WIN'),
        ('LOSE', 'LOSE'),
        ('PENDING', 'PENDING'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    bet = models.IntegerField(default=5)
    choice = models.CharField(choices=BET_CHOICES,max_length=50, null=True,blank=True)
    status = models.CharField(choices=WIN_OR_LOSE, max_length=50,default='PENDING')
    result = models.ForeignKey(Result, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.choice

