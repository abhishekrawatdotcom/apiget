from django.db import models
class apimodel(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    
    add=models.CharField(max_length=50)
    

