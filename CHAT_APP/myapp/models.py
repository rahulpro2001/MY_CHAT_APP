from email.policy import default
from sre_constants import MAX_UNTIL
from time import thread_time
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

# Create your models here.
# creating the db for room and for messsage after that 
# run migratiion
# than register model with admin
# user name ----- rahul_admin
# pass--Rahul1999

class Room(models.Model):
    name = models.CharField(max_length = 20)
    
class Message(models.Model):
    value = models.CharField(max_length = 1000)
    date = models.DateTimeField(default=datetime.now,blank = True)
    room = models.IntegerField(max_length = 1000)
    user = models.CharField(max_length = 1000 , default="unknown user")
