from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Books(models.Model):
    titulo=models.CharField(max_length=60)
    autor=models.CharField(max_length=50)
    genero = models.CharField(max_length=60)
    image= models.ImageField(upload_to='books',null=True)