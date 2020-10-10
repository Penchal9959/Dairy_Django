#models.py
from django.db import models
 
# Create your models here.  
class Member(models.Model):
    # firstname=models.CharField(max_length=30)
    # lastname=models.CharField(max_length=30)
    username=models.CharField(blank=True, null=True,max_length=30)
    password=models.CharField(blank=True, null=True,max_length=20)
    
    # def __str__(self):
    #     return self.firstname + " " + self.lastname
   
  
    # class Meta:  
    #     db_table = "web_member"from django.db import models

# Create your models here.
class text(models.Model):
	Dairy = models.TextField(blank=True, null=True,max_length=10000)
 
