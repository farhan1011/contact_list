from django.db import models

# Create your models here.
class Contact(models.Model):

    def __str__(self):
        return self.full_name

    full_name=models.CharField(max_length=100)
    relationship=models.CharField(max_length=50)
    email=models.EmailField(max_length=200)
    phone_number=models.CharField(max_length=50)
    addres=models.CharField(max_length=150)


