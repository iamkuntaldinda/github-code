from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=40, null=True)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15, null=True)
    message = models.CharField(max_length=2000, null=True)
    def __str__(self):
    	return [self.nae,self.email,self.phone,self.message]
    
    