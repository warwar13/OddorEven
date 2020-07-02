from django.db import models
from home.models import *
from .views import *
from home.views import *
from django.utils.timezone import now #import timezone

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

#==================== Sandy model structure =======================//
BET_CHOICES = (
    ('ODD', 'ODD'),
    ('EVEN', 'EVEN'),
)

class Bet_Room(models.Model):
    room_name = models.CharField(max_length=150,null=False,blank=False)
    result = models.CharField(choices=BET_CHOICES,max_length=50, null=True,blank=True) #initialize with null
    participants = models.ManyToManyField(User, through='Bet_Participants') #returns list of participants
    is_open = models.BooleanField(default=True)
    is_finish = models.BooleanField(default=False)

    def __str__(self):
        return self.room_name

    def get_result(self):
        return self.result

class Bet_Participants(models.Model):
    bet = models.IntegerField(default=0)
    choice = models.CharField(choices=BET_CHOICES,max_length=50, null=False,blank=False)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Bet_Room, on_delete=models.CASCADE)
    date_participate = models.DateTimeField(default=now)

    def result(self):
        if self.room.get_result == self.choice:
            return "WIN"
        else:
            return "LOSE"
