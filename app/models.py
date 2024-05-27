from django.db import models

# Create your models here.
class Product(models.Model):
   
    Name=models.CharField(max_length=25)
    Number=models.CharField(max_length=6)
    
    Cost=models.CharField(max_length=6)

    def _str_(self):
        return self.Name
