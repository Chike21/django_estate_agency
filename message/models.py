from django.db import models
from datetime import datetime
from accounts.models import Users

# Create your models here.
class MyMessages(models.Model):
    agent_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING, default="0") 
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    comment = models.TextField()
    pname = models.CharField(max_length=255)
    plocation = models.CharField(max_length=255)
    msg_date = models.DateTimeField(auto_now_add=True, blank=True)
    
    def _str_(self):
        return self.name